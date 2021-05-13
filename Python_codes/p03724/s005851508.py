from collections import Counter
N,M=map(int, input().split())
Q=[]
for _ in range(M):
    a,b=map(int, input().split())
    Q.append(a)
    Q.append(b)
C=Counter(Q)
for c in C.values():
    if c&1:
        print('NO')
        exit()
print('YES')