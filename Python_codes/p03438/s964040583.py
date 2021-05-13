N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = max(0, sum(B) - sum(A))
ca = 0
cb = 0

for a, b in zip(A, B):
    if a < b:
        ca += (b - a + 1) // 2
        cb += (b - a) % 2
    if a > b:
        cb += a - b

if c < max(ca, cb):
    print('No')
else:
    print('Yes')
