H, W, K, *S = open(0).read().split()

A = []
color = 0
pivot = 0
for i, s in enumerate(S):
    r = s.find("#")
    if r != -1:
        pivot = i
        T = []
        l = -1
        while r != -1:
            color += 1
            T += [color] * (r - l)
            l, r = r, s.find("#", r + 1)
        T += [color] * (len(s) - l - 1)
        A.append(T)
    else:
        A.append(-1)

for i in reversed(range(pivot)):
    if A[i] == -1:
        A[i] = A[i + 1]

for i in range(pivot + 1, len(A)):
    if A[i] == -1:
        A[i] = A[i - 1]

for a in A:
    print(*a)
