H, W, K, *S = open(0).read().split()
H, W = int(H), int(W)

A = []
c = 0
for i, s in enumerate(S):
    T = []
    r = s.find("#")
    l = -1
    while r != -1:
        c += 1
        T += [c] * (r - l)
        l, r = r, s.find("#", r + 1)
    T += [c] * ((W - l - 1) % W)
    A.append(T)

for i in reversed(range(H - 1)):
    if not A[i]:
        A[i] = A[i + 1]

for i in range(1, H):
    if not A[i]:
        A[i] = A[i - 1]

for a in A:
    print(*a)