import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

r = 0
tmp = 0
ans = 0
for l in range(N):
    while r < N:
        if tmp ^ A[r] == tmp + A[r]:
            tmp += A[r]
            r += 1
        else:
            ans += r - l
            tmp -= A[l]
            break
    else:
        ans += r - l
print(ans)