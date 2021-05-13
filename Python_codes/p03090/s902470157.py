N = int(input())

group_sum = N if N % 2 == 1 else N + 1

ans = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i + j != group_sum:
            ans.append([i, j])

print(len(ans))
for edge in ans:
    print(" ".join(map(str, edge)))
