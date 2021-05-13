N = int(input())
A = list(map(int, input().split()))
count = 0
for x in range(N):
    find = A[x]
    if A[find - 1] - 1 == x:
        count += 1
print(count // 2)
