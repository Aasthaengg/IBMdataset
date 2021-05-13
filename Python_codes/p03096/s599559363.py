mod = 1000000007

N = int(input())
C = []
for i in range(N):
    c = int(input())
    if i == 0 or C[-1] != c:
        C.append(c)
cases = [1] * (len(C) + 1)
indexes = dict()
for i in range(1, 1 + len(C)):
    c = C[i - 1]
    if c not in indexes:
        cases[i] = cases[i - 1]
    else:
        cases[i] = (cases[i - 1] + cases[indexes[c]]) % mod
    indexes[c] = i
print(cases[len(C)])
