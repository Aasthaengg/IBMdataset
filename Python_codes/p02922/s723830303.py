A,B = map(int,input().split())
ans = 0
while True:
    if A*ans-(ans-1) >= B:
              print(ans)
              break
    else:
        ans += 1