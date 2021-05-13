A = [ord(a) - 97 for a in input()]
N = len(A)
D = {}
ans = N * (N - 1) // 2 + 1
for i, a in enumerate(A):
    if a in D:
        ans -= D[a]
        D[a] += 1
    else:
        D[a] = 1
print(ans)