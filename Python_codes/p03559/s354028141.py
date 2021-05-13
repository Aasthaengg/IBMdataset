n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
a.reverse()
b.sort()
b.reverse()
c.sort()
c.reverse()
c.append(0)

i=0
l=[]
for j in b:
  while c[i]>j:
    i+=1
  l.append(i)
b.append(0)
s=0
cnt=0
i=0
for j in a:
  while b[i]>j:
    s+=l[i]
    i+=1
  cnt+=s
print(cnt)