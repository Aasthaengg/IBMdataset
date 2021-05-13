from collections import Counter
N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))

d=Counter(D)
for i in range(M):
    if T[i] not in d or d[T[i]]==0:
        print('NO')
        exit()
    d[T[i]]-=1
print('YES')