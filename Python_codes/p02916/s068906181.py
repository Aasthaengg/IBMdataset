n = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
prev = -10
for a in A:
    ans += B[a]
    if a == prev + 1:
        ans += C[prev]
    prev = a
print(ans)
