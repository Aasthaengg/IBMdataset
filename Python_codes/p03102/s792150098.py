N, M, C = [int(x) for x in input().split()]
B = list([int(x) for x in input().split()])

count = 0
for _ in range(N):
    A = list([int(x) for x in input().split()])

    solve = 0
    for i in range(M):
        solve += A[i] * B[i]
    solve += C

    if solve > 0:
        count += 1

print(count)
