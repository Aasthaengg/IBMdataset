N = int(input())
A = list(map(int, input().split()))

ans = 0
be = A[0]
for ai in A[1:]:
    if be == ai:
        ans += 1
        be = -1
    else:
        be = ai

print(ans)
