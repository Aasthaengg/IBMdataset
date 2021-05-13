N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
op = []
for i in range(M):
    b, c = map(int, input().split())
    op.append((c, b))
op.sort(reverse=True)
sum = 0
j = 0
for c,b in op:
    while j < N and b > 0 and A[j] < c:
        sum += c
        b -= 1
        j = j + 1
while j < N:
    sum += A[j]
    j += 1
print(sum)