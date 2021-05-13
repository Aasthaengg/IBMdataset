n=int(input())
l=list(map(int,input().split()))
a=l[0]
b=0
c=[]
for i in range(1,n):
  if l[i]==a:
    b+=1
  else:
    c.append(b)
    b=0
  a=l[i]
c.append(b)
for i in range(len(c)):
  c[i]=(c[i]+1)//2
print(sum(c))