N = int(input())
A = [int(x) for x in input().split(" ")]
flag = True
swap_count = 0
i = 0
while flag:
    flag = False
    for j in range(N-1, i, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            flag = True
            swap_count += 1
    i += 1

print(*A)
print(swap_count)