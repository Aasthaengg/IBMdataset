N,Q=map(int,input().split())
S=input()
lr=[list(map(int,input().split()))for _ in range(Q)]

count=[0]+[0]*(N-1)
i=1
while i<N:
    if S[i-1]=='A' and S[i]=='C':
        count[i]=count[i-1]+1
    else:
        count[i]=count[i-1]
    i+=1

for l,r in lr:
    print(count[r-1]-count[l-1])