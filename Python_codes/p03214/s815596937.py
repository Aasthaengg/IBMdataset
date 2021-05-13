N = int(input())
A = list(map(int, input().split()))

avg = sum(A) / N

L = []
for i in range(N):
    L.append((i, abs(avg - A[i])))

L.sort(key=lambda x: (x[1], x[0]))

print(L[0][0])