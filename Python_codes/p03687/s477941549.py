def check(S):
    cond=True
    for i in range(len(S)-1):
        if S[i]!=S[i+1]:
            cond=False
    return cond

def shrink(t,s):
    tt=[]
    for i in range(len(t)-1):
        if t[i+1]==s:
            tt.append(t[i+1])
        else:
            tt.append(t[i])
    return tt

S=input()
N=len(S)
ans=N

for i in range(N):
    s=S[i]
    t=list(S)
    for j in range(N):
        if check(t):
            break
        t=shrink(t,s)
    ans=min(ans,j)
print(ans)