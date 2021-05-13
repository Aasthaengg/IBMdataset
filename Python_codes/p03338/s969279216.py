N = int(input())
S = input()

ans = 0

for i in range(1, N):
    a = S[:i]
    b = S[i:]
    # print(i, a, b)
    a = set(a)
    b = set(b)
    c = a & b
    # print(c)
    n = len(c)
    ans = max(ans, n)

print(ans)
