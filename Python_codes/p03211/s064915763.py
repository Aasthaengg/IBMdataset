S = list(map(int, list(input())))
min_n = 10**4
for i in range(len(S) - 2):
    a, b, c = S[i], S[i+1], S[i+2]
    n = abs(100 * a + 10 * b + c - 753)
    min_n = min(min_n, n)
print(min_n)
