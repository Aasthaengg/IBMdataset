n=int(input())
def ryuka(x):
  return l[x-1]+l[x-2]

l=[2]+[1]+[0]*(n-1)
for i in range(2,n+1):
  l[i]=ryuka(i)
print(l[n])