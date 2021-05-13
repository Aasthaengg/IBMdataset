S=input()
L=(len(S)-1)//2
ans='Yes'
if S[:L]!=S[-L:]:
    ans='No'
for n in range(L):
    m=L-1-n
    if S[n]!=S[m]:
        ans='No'
print(ans)