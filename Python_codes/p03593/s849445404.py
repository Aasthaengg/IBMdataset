from collections import Counter

def solve(h, w, a):
    c = Counter(list("".join(a)))
    g = [0] * 3
    for num in c.values():
        g[0] += int(num % 2 == 1)
        g[1] += 2 * int(num % 4 == 2)
        g[2] += (num // 4) * 4
    if (w % 2 == 0) and (h % 2 == 0):
        return "Yes" if (g[2] == h*w) else "No"
    if (w % 2 == 1) and (h % 2 == 1):
        return "Yes" if (g[0] == 1) and g[1] <= (h + w - 2) else "No"
    if w % 2 == 1:
        return "Yes" if (g[0] == 0) and (g[1] <= h) else "No"
    if h % 2 == 1:
        return "Yes" if (g[0] == 0) and (g[1] <= w) else "No"
    return "Yes"

h, w = map(int, input().split())
a = [input() for r in range(h)]
print(solve(h, w, a))