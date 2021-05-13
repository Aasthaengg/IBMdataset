N = int(input())
A = list(map(int, input().split()))
sA = [A[0]]
d = []
for i in range(1, N):
    sA.append(sA[-1] + A[i])

for i in range(N):
    d.append(abs(sA[i] - (sA[-1] - sA[i])))
print(min(d))
