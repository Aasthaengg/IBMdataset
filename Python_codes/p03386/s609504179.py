A,B,K=map(int,input().split())
S=(set(range(A,A+K))|set(range(B-(K-1),B+1)))
S=list(S)
S.sort()

for x in S:
    if A<=x<=B:
        print(x)
