n, m=map(int, input().split())
gate=[]

for i in range(m):
    L, R=map(int, input().split())
    gate.append((L, R))

L_max=0
R_min=10**6
for i in range(m):
    if gate[i][0]>L_max:
        L_max=gate[i][0]

for i in range(m):
    if gate[i][1]<R_min:
        R_min=gate[i][1]


ans=0

for i in range(1, n+1):
    if L_max<=i<=R_min:
        ans+=1

print(ans)