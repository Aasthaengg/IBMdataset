N, X = map(int, input().split())
L = [0] + list(map(int, input().split()))

s = 0
S = []
for i in range(N+1):
    s += L[i]
    S.append(s)

c = 0
for s in S:
    if s <= X:
        c += 1
print(c)
