n,x,y=map(int,input().split())
x-=1
y-=1
L=[0]*(n-1)
for i in range(n-1):
    for j in range(i+1,n):
        if j<=x or i>=y:
            L[j-i-1]+=1
        elif i<=x and y<=j:
            L[x-i+j-y]+=1
        else:
            a=j-i
            b=abs(x-i)+1+abs(y-j)
            L[min(a,b)-1]+=1
for k in L:
    print(k)            