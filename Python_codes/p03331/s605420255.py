N = int(input())
ans = float("inf")

for i in range(1, N):
    A = i
    B = N - i
    A_sum = 0
    B_sum = 0
    while True:
        if A // 10 > 0:
            A_sum += A % 10
            A  //= 10
        else:
            A_sum += A % 10
            break
    while True:
        if B // 10 > 0:
            B_sum += B % 10
            B  //= 10
        else:
            B_sum += B % 10
            break
    if ans > (A_sum + B_sum):
        ans = A_sum + B_sum
print(ans)
