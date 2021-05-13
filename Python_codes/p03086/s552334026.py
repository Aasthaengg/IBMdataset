#b
S=input()

l = len(S)
ans=0
for i in range(l):
    for j in range(i,l):
        ss = S[i:j+1]
        if all(sss in ["A","G","C","T"] for sss in ss):
            cand = len(ss)
            ans=max(ans,cand)
print(ans)