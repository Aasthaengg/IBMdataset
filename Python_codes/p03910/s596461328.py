N=int(input())
ans=0
reject=0
A=[]
for i in range(1,N+1):
    ans+=i
    if ans>=N:
        reject=ans-N
        for j in range(1,i+1):
            if j!=reject:
                print(j)
        break