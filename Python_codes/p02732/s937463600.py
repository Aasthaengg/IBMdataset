n = int(input())
A = list(map(int,input().split()))

S={}
for i in range(n):
    a = A[i]
    if a in S :
        S[a]+=1
    else:
        S[a]=1

V=list(S.values())
c = sum([v*(v-1)//2 for v in V])

cdiff=0
K=[]
for i in range(n):
    cdiff=0
    a = A[i]
    s=S[a]
    if s>=2 :
        cdiff=(s*(s-1)-(s-1)*(s-2))//2
    print(c-cdiff)



