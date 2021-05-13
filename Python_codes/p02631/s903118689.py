n=int(input())
a=list(map(int,input().split()))
c=[]
x=0
for i in a:x^=i
for i in a:c.append(i^x)
print(*c)