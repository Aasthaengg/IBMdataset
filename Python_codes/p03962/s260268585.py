a,b,c=map(int,input().split())
i=0
if a!=b:
    i+=1
if a!=c:
    i+=1
if b!=c:
    i+=1
if i==0:
    i+=1
print(i)
