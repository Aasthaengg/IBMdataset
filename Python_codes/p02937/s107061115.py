from bisect import bisect_right as br
S=input()
T=input()

def s2n(s):
    return ord(s)-97

ALF=[[] for _ in [0]*26]
for i in range(len(S)):
    ALF[s2n(S[i])].append(i)

ALF_T=[0]*26
seqT=[]
res=0
for t in T:
    i=s2n(t)
    if ALF[i]:
        if seqT:
            a=seqT[-1]
        else:
            a=-1
        j=br(ALF[i],a)
        seqT.append(ALF[i][j%len(ALF[i])])
    else:
        res=-1
if res>=0:
    tmp=[]
    m=-1
    for n in seqT:
        if m<n:
            tmp.append(n)
        else:
            res+=1
            tmp=[n]
        m=n
    res=res*len(S)+tmp[-1]+1
print(res)