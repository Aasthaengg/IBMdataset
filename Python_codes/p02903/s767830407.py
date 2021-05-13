H, W, A, B = map(int, input().split())

ans = []

for _ in range(H - B):
    a = ['0'] * (W - A)
    a.extend(['1'] * A)
    ans.append(a)
for _ in range(B):
    a = ['1'] * (W - A)
    a.extend(['0'] * A)
    ans.append(a)

for a in ans:
    print(*a, sep='')
