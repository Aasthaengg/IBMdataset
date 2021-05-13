N = int(input())
result = []

for A in range(1, N):
    B = N - A
    A = str(A)
    B = str(B)
    A_sum = sum(list(map(int, A)))
    B_sum = sum(list(map(int, B)))
    result.append(A_sum + B_sum)

print(min(result))
