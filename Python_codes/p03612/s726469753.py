N = int(input())
p = list(map(int,input().split()))

ans = 0
continuous_flag= 0

for n in range(N):
  if p[n] == n+1:
    if continuous_flag == 0:
      ans += 1
      continuous_flag = 1
    else:
      continuous_flag = 0
  else:
    continuous_flag = 0
print(ans)