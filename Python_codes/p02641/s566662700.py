x,n=map(int,input().split())
p=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,102):
  if i not in p:
    a.append(i)
#a=set(a)

for i in a:
  b.append(abs(x-i))
#print(a)
idx = b.index(min(b))

print(a[idx])