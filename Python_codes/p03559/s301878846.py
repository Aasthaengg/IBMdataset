n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
i,j,k=0,0,0
m1=[]
while k<n and i<n:
  if b[i]>a[k]:
    j+=1
    k+=1
  else:
    m1.append(j)
    i+=1
for t in range(len(m1),len(b)):
  m1.append(j)
i,j,k=0,0,0
m2=[]
while k<n and i<n:
  if c[i]>b[k]:
    j+=m1[k]
    k+=1
  else:
    m2.append(j)
    i+=1
for t in range(len(m2),len(c)):
  m2.append(j)
print(sum(m2))