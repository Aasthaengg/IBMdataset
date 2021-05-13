N = int(input())
A = [int(a) for a in input().split()]

ans = 0
j = 1
k = 0
sum_plus = A[0]
sum_xor = A[0]
while j <= N and k < j:
    if sum_plus == sum_xor:
        ans += j-k
        if j < N:
            sum_plus += A[j]
            sum_xor ^= A[j]
        j += 1
    else:
        sum_plus -= A[k]
        sum_xor ^= A[k]
        k += 1
    
print(ans)