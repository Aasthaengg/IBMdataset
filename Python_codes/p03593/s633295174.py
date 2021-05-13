h, w = map(int, input().split())
alphcnt = [0] * 26
for _ in range(h):
    a = list(input())
    for x in a:
        alphcnt[ord(x) - 97] += 1
p1, p2, p4 = 0, 0, 0
for i in range(26):
    x = alphcnt[i] // 4
    alphcnt[i] -= 4 * x
    p4 += x
for i in range(26):
    x = alphcnt[i] // 2
    alphcnt[i] -= 2 * x
    p2 += x
for i in range(26):
    x = alphcnt[i]
    alphcnt[i] -= x
    p1 += x
t = 0
if h % 2 == w % 2 == 0:
    if p1 == p2 == 0:
        t = 1
elif h % 2 == w % 2 == 1:
    if p1 == 1 and p4 >= (h // 2) * (w // 2):
        t = 1
else:
    if p1 == 0 and p4 >= (h // 2) * (w // 2):
        t = 1
print("Yes" if t == 1 else "No")