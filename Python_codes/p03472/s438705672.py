N,H = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
ab.sort(key = lambda x:x[0],reverse = True)
swing = ab[0][0]
ans = 0
if H<= ab[0][1]:
    print(1)
else:
    ab.sort(key = lambda x:x[1],reverse = True)
    for i in range(N):
      if ab[i][1] < swing:
          continue
      H -= ab[i][1]
      ans += 1
      if H <= 0:
          break
    else:
        if H % swing == 0:
            ans += H//swing
        else:
            ans += H//swing +1
    print(ans)
