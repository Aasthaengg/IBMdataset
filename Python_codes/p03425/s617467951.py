import sys
input = sys.stdin.readline


n = int(input().strip())


d = {
    "M": 0,
    "A": 0,
    "R": 0,
    "C": 0,
    "H": 0
}
top = list("MARCH")


for _ in range(n):
    name = input().strip()
    if name[0] in top:
        d[name[0]] += 1

ans = 0

for a in range(3):
    for b in range(a + 1, 4):
        for c in range(b + 1, 5):
            ans += d[top[a]] * d[top[b]] * d[top[c]]

print(ans)
