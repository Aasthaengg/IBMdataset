n,m=map(int,input().split())
PY=sorted([list(map(int,input().split()))+[_] for _ in range(m)],key=lambda x:x[1])

A,B={},[]
for p,y,num in PY:
    if p not in A:
        A[p]=1
        B.append([p,A[p],num])
    else:
        A[p] +=1
        B.append([p,A[p],num])

for a,b,c in sorted(B,key=lambda x:x[2]):
    print(str(a).zfill(6)+str(b).zfill(6))