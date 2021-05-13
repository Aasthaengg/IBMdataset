n,m=map(int,input().split())
c=0
for i in range(n,m+1):
    s=str(i)
    if(s==s[::-1]):
        c=c+1
print(c)
