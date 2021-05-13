n = int(input())
A = tuple(map(lambda x:int(x)-1, input().split()))

paired = [0] * n
c = 0
for i in range(n-1):
    if paired[i]:
        continue

    if A[A[i]] == i:
        c += 1
        paired[A[i]] = 1

print(c)
