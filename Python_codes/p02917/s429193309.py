N = int(input())
B = list(map(int, input().split()))

A_sum = B[0]
for i in range(N-1):
    if i != N-2:
        A_sum += min(B[i], B[i+1])
    else:
        A_sum += B[i]

print(A_sum)