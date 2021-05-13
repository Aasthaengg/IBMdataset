R,G,B,N=map(int,input().split())
ans=0
 
for i in range(N//R+1):
    for j in range((N-R*i)//G+1):
        b=N-(R*i+G*j)
        if b==0 or  b%B==0: 
            ans+=1
 
print(ans)