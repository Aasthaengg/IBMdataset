N,Q=map(int,input().split())
S=list(input())
answers=[0 for _ in range(N)]
for n in range(1,N):
    if S[n]=='C':
        if S[n-1]=='A':
            answers[n]=answers[n-1]+1
        else:
            answers[n]=answers[n-1]
    else:
        answers[n]=answers[n-1]


for _ in range(Q):
    l,r=map(int,input().split())
    print(answers[r-1]-answers[l-1])
