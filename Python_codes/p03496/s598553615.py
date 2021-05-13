N = int(input())
A = list(map(int, input().split()))

large = -float('inf')
small = float('inf')
for i, a in enumerate(A):
    if large < a:
        large = a
        idxL = i + 1
    if small > a:
        small = a
        idxS = i + 1

S = [(i + 1, i + 2) for i in range(N - 1)]
S_reverse = [(i, i - 1) for i in range(N, 1, -1)]

if small >= 0:
    ans = S
elif large <= 0:
    ans = S_reverse
elif abs(large) >= abs(small):
    ans = [(idxL, i) for i in range(1, N + 1) if i != idxL] + S
else:
    ans = [(idxS, i) for i in range(1, N + 1) if i != idxS] + S_reverse

print(len(ans))
for s in ans:
    print(*s)
