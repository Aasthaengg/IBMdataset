N= int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
ans=[]

if N==1:
    print(A1[0]+A2[0])
    exit()
else:
    for i in range(N):
        ansA1=0
        ansA2=0
        for j in range(i+1):
            ansA1+=A1[j]
        for k in range(j,N):
            ansA2+=A2[k]
        ans1=ansA1+ansA2
        ans.append(ans1)

print(max(ans))