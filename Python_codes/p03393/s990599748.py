S=list(input())
abc=list("abcdefghijklmnopqrstuvwxyz")
idx={}
for i in range(26):
    idx[abc[i]]=i
D=[0]*26
for s in S:
    D[idx[s]]+=1

if len(S)!=26:
    for i in range(26):
        if D[idx[abc[i]]]==0:
            ans="".join(S)+abc[i]
            break
        
else:
    ans=-1
    now=S[-1]
    for i in range(len(S)-1, 0,-1):
        if idx[S[i]]> idx[S[i-1]]:
            now=sorted(list(now))

            for j,n in enumerate(now):
                if idx[n]>idx[S[i-1]]:
                    pre=n
                    ans="".join(S[:i-1])+pre
                    print(ans)
                    exit()



        else:
            now=str(now)
            now+=S[i-1]

print(ans)
