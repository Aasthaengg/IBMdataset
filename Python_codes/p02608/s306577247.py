N=int(input())
ans=[0]*(N+1)
rN=int(N**(1/2))
for x in range(1,rN+1):
    for y in range(1,rN+1):
        for z in range(1,rN+1):
            n=x**2+y**2+z**2+x*y+y*z+z*x
            if n<=N:
                ans[n]+=1
                
for i in range(1,N+1):
    print(ans[i])