n = int(input())
A = list(map(int, input().split()))

ans = 0
r = 0
bit_check = 0
for l in range(n):
    while r <= n-1:
        num = A[r]
        if num & bit_check == 0:
            bit_check |= num
            r += 1
        else:
            bit_check -= A[l]
            break
    ans += r - l

print(ans)