N = int(input())
A = tuple(map(int, input().split()))

i, j = 0, 0
s = 0
ans = 0
while i < N:
    if s | A[i] != s + A[i]:
        s -= A[j]
        j += 1
    else:
        s += A[i]
        i += 1
        ans += i - j
print(ans)
