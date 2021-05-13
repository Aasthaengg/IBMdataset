n=int(input())
ans=0
cnt=[0]*500000
#print(2*10**2)
for i in range(1,2*10**2+1):
    for j in range(1,2*10**2+1):
        for k in range(1,2*10**2+1):
            cnt[((i+j)**2+(j+k)**2+(k+i)**2)//2-1]+=1
for i in range(n):
    print(cnt[i])
