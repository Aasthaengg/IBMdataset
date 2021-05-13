S=input()
A=['A','G','T','C']
ans=0
cnt=0
N=len(S)

for i in range(N):
    cnt=0
    for j in range(0,N-i):
        if S[i+j] in A:
            cnt+=1
        else:
            break
    ans=max(ans,cnt)
print(ans)