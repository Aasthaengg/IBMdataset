N = int(input())
a = [0] + list(map(int, input().split()))
b = [0] * (N+1)
M = 0
for i in range(N, 0, -1):
    temp_sum = sum([b[j] for j in range(i, N+1, i)]) - b[i]
    if temp_sum % 2 == 0 and a[i] == 0:
        b[i] = 0
    if temp_sum % 2 == 1 and a[i] == 0:
        b[i] = 1
        M += 1
    if temp_sum % 2 == 0 and a[i] == 1:
        b[i] = 1
        M += 1
    if temp_sum % 2 == 1 and a[i] == 1:
        b[i] = 0


print(M)
ans_list = [i for i in range(1, N+1) if not b[i] == 0]
print(*ans_list)