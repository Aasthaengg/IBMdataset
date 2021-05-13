N , M = map(int,input().split())
C = list(map(int,input().split()))
r = 0
for i in range(M):
    r += C[i]

a = N - r
if a >= 0:
    print(a)
else:
    print('-1')