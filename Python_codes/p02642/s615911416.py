N=int(input())
A=list(map(int,input().split()))
A.sort()
TF={a:True for a in A}
for i in range(N):
    if TF[A[i]]==True:
        if i > 0 and A[i - 1] == A[i]:
            TF[A[i]] = False
        m=A[N-1]//A[i]
        for j in range(2,m+1):
            s=A[i]*j
            if s in TF:
                TF[s]=False
print(len([1 for a in A if TF[a]==True]))