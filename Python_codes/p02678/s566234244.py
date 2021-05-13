N, M = map(int, input().split())

A = []
B = []

for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

P = [[] for _ in range(N + 1)]

for a, b in zip(A, B):
    P[b].append(a)
    P[a].append(b)

ans = [0] * (N + 1)
ans[1] = 1
next_numbers = [1]

while next_numbers:
    check_number = next_numbers[:]
    next_numbers = []
    for number in check_number:
        for x in P[number]:
            if ans[x] == 0:
                ans[x] = number
                next_numbers.append(x)

print('Yes')
for i in range(2, N + 1):
    print(ans[i])