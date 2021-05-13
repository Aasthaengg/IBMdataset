n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
ans = 0
a.append(-1)
x = []
tmp = 0
for i in range(n):
  if a[i] != a[i+1]:
    tmp += 1
    x.append(tmp)
    tmp = 0
  else:
    tmp += 1
    
x.sort(reverse=True)
print(sum(x[k:]))