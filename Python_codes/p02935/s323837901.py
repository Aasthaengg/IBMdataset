N = int(input())
l = list(map(int,input().split()))
ans = 0
l.sort()
for i in range(N):
  ans += l[i]
  if i >= 1:
    ans /= 2
print(ans)