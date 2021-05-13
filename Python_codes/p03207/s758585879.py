n=int(input())
p = [0]*n
for i in range(0,n):
  p[i]=int(input())
p.sort()
p[n-1]=int(p[n-1]/2)
print(sum(p))
