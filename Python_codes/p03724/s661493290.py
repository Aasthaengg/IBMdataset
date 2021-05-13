N, M = map(int,input().split())
C = [0]*N

for k in range(M):
    a, b = map(int,input().split())
    C[a-1] += 1
    C[b-1] += 1

for e in C:
    if e%2 != 0:
        print("NO")
        exit(0)
print("YES")
