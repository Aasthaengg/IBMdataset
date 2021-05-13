n=int(input())
a,f,b=sorted([list(map(int,input().split())) for i in range(n)],key=lambda x:x[1]),1,0
for i in range(n):
    b+=a[i][0] 
    if b>a[i][1]: 
        f=0 
print('Yes' if f==1 else 'No')