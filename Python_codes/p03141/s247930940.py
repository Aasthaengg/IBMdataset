n = int(input())
l = []
ans = 0
for i in range(n):
  a,b = map(int,input().split())
  ans += a
  l.append(a+b)
l.sort(reverse = True)
for i in range(n):
  ans -= l[i]*(i%2==1)
print(ans)