n=int(input())
#n,m = map(int,input().split())

S={}
for i in range(n):
    a,b = map(int,input().split())
    if b in S:
        S[b]+=a
    else:
        S[b]=a
    
S2=sorted(S.items())
wa=0
for i in range(len(S2)):
    s,w = S2[i]
    wa+=w
    if s<wa :
        print("No")
        exit()

print("Yes")
