N = int(input())
p = list(map(int,input().split()))
k = sorted(p)
ans = 0
for i in range(N):
  if k[i] != p[i]:
    ans += 1
if ans == 0 or ans == 2:
  print("YES")
else:
  print("NO")