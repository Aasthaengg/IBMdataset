n = int(input())
a = list(map(int,input().split()))
ans = 1
l = []
for i in range(n):
  ans = ans*a[i]
for i in range(n):
  l.append(ans/a[i])
print(ans/sum(l))