N=int(input())
ab=[[]for _ in range(N)]
for i in range(N):
    a,b=map(int,input().split())
    ab[i]=[a+b,a,b]

ab.sort()
ab=ab[::-1]

T=A=0
for i in range(N):
    if i%2:
        A+=ab[i][2]
    else:
        T+=ab[i][1]
print(T-A)