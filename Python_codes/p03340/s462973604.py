N = int(input())
*A, = map(int, input().split())
right = 0; ans = 0; S = 0; S_xor = 0;
for left in range(N):
    while right < N and S_xor ^ A[right] == S + A[right]:
        S_xor ^= A[right]
        S += A[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        S_xor ^= A[left]
        S -= A[left]
print(ans)