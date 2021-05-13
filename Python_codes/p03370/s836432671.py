n,x=map(int,input().split())
a=[]
for i in range(n):
    m=int(input())
    a.append(m)
count=0
if x>=sum(a):
    count+=n
    x-=sum(a)
while x>=min(a):
    count+=1
    x-=min(a)
print(count)