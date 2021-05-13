S=list(input())
S=list(map(int,S))
K=int(input())

i=0
while i<K:
    if S[i]>1:
        ans=S[i]
        break
    else:
        ans=1
        i+=1
print(ans)
