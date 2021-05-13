n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = a[0]
for i in range(1,n):
  a1 = a[i]
  ans = (ans + a1)/2
print(ans)