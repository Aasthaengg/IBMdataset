pf = {}
ans = 1
m = int(input())
for i in range(2, m+1):
    for j in range(2, int(i**0.5)+1):
        while i%j==0:
            pf[j]=pf.get(j,0)+1
            i//=j
    if i>1:
        if i in pf.keys():
            pf[i]+=1
        else:
            pf[i]=1

for v in pf.values():
    ans *= v+1
print(ans%(10**9+7))