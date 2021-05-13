N=int(input())

ans=[0]*N

for x in range(1,int(N**(1/2))):
    for y in range(1,int(N**(1/2))):
        for z in range(1,int(N**(1/2))):
            cnt=x**2+y**2+z**2+x*y+y*z+z*x
            if cnt>N:
                break
            else:
                ans[cnt-1]+=1
for i in range(N):
    print(ans[i])