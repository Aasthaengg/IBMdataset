ans=0
A=[]
B=[]
for _ in range(int(input())):
    i,j=map(int,input().split())
    A+=[i]
    B+=[j]
for a,b in zip(A[::-1],B[::-1]):    
    if (a+ans)%b:
        ans+=b-(a+ans)%b
print(ans)