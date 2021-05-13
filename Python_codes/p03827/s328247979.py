n=int(input())
s= input().strip()
x=0
c=[0]*(n+1)
c[0]=0
for i in range(n):
    if s[i]=='I':
        x=x+1
    else:
        x=x-1
    c[i]=x
print(max(c))