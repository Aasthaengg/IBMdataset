N=int(input())
l=[2,1]
for i in range(2,N+1):
  k=l[i-2]+l[i-1]
  l.append(k)
print(l[N])