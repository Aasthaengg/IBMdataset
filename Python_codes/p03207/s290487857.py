n=int(input())
a=[]
for i in range(n):
  p=int(input())
  a.append(p)

a.sort()
s=a[n-1]//2
print(sum(a)-s)