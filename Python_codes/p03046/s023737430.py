def solve(m, k):
    if k >= 2**m:
        return -1
    if (m == 1) and (k == 0):
        return "0 0 1 1"
    if (m == 1) and (k == 1):
        return -1
    b = [x for x in range(2**m) if x != k]
    c = b[::-1]
    a = b + [k] + c + [k]
    return " ".join(map(str, a))

m, k = map(int, input().split())
print(solve(m, k))