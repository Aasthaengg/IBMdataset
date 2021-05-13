n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a = list(map(lambda x:x-1, a))
ans = 0
for i in range(n):
  ans += b[a[i]]
  if i > 0 and a[i-1] + 1 == a[i]:
    ans += c[a[i-1]]
print(ans)