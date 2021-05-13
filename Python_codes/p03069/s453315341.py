N=int(input())
S=list(map(lambda x:1*(x=="#"),input()))

L=M=S.count(0)

for i in range(N):
    if S[i]:
        M+=1
    else:
        M-=1
        L=min(L,M)
print(L)