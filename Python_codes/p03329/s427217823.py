N = int(input())

def to_n(X, n):
    if (int(X / n)):  return to_n(int(X / n), n) + str(X % n)
    return str(X % n)

ans = 10 ** 9 + 7
for i in range(N + 1):
    N6 = to_n(N - i, 6)
    N9 = to_n(i, 9)
    res = 0
    for j in N6:  res += int(j)
    for j in N9:  res += int(j)
    ans = min(res, ans)
print(ans)