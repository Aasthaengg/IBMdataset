N, K, Q = map(int, input().split())
data = [0]*N
for _ in range(Q):
    A = int(input())
    A -= 1
    data[A] += 1
print(*list("Yes" if K-Q+x>0 else "No" for x in data), sep="\n")