n,k,c=map(int, input().split())
s=list(input())
L=[]
R=[]

i=0
while i<n: # 前から貪欲に働く日を決定している。
    if s[i]=='o':
        L.append(i+1)
        i+=(c+1)
    else:
        i+=1

j=0
s2=s[::-1]
while j<n: # 後ろから貪欲に働く日を決定している。
    if s2[j]=='o':
        R.append(n-j)
        j+=(c+1)
    else:
        j+=1
R=R[::-1]        

if len(L)<=k:
    for p in range(min(len(L),len(R))):
        if L[p]==R[p]:
            print(L[p])