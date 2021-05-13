N=int(input())
B=[1]*55556

B[0]=0
B[1]=0
for i in range(2,55556):
    if B[i]==0:continue
    temp=i
    cnt=2
    while temp*cnt<=55555:
        B[temp*cnt]=0
        cnt+=1
PN=[]
for i in range(2,55556):
    if B[i]:
        PN.append(i)

for i in range(1,10,2):
    cnt=1
    ans=[2]
    for p in PN:
        if p%10==i:
            ans.append(p)
            cnt+=1
            if cnt==N:
                print(*ans)
                exit()

