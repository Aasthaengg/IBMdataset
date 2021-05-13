N = int(input())
A = [int(input()) for _ in range(N)]

sort_A = sorted(A, reverse=True)
max_value = sort_A[0]
second_value = sort_A[1]

ans = []

for a in A:
    if a < max_value:
        ans.append(max_value)
    elif a == max_value:
        ans.append(second_value)

print(*ans, sep='\n')
