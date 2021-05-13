N, M = map(int, input().split())

D = [0]*M

for i in range(N):
    A = list(map(int, input().split()))
    A.pop(0)
    for j in A:
        D[j-1] += 1

print(D.count(N))