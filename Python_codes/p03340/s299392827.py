N = int(input())
A = list(map(int, input().split()))

def ischeck(amount, target):
    for i in range(30):
        a = (amount >> i) & 1
        b = (target >> i) & 1
        if a & b:
            return False
    return True

ans = 0
tmp = A[0]
r = 0
for l in range(N):
    if r == l:
        tmp = A[l]
        r += 1
    while r < N and ischeck(tmp, A[r]):
        tmp += A[r]
        r += 1
    ans += (r - l)
    tmp -= A[l]

print(ans)
