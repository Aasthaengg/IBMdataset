N = int(input())
h = list(map(int, input().split()))

ans = 0
while sum(h) > 0:
  flag = False
  for i in range(N):
    if flag:
      if h[i] == 0:
        flag = False
        ans += 1
      else:
        h[i] -= 1
        if i == N-1:
          ans += 1
    else:
      if h[i] > 0:
        h[i] -= 1
        flag = True
        if i == N-1:
          ans += 1
          flag = False
print(ans)