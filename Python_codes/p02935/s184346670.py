n = int(input())
v = list(map(int,input().split()))
v.sort()
ans = v[0]
for i in range(1,n):
  ans += v[i]
  ans /= 2
print(ans)