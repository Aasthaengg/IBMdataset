n, q = map(int, input().split())
s = input()
q = [tuple(map(int, input().split())) for i in range(q)]

ans = 0
t = [0]
for i in range(1, n):
    if s[i - 1:i + 1] == "AC":
        t.append(t[i - 1] + 1)
    else:
        t.append(t[i - 1])
# print(t)
for l, r in q:
    print(t[r - 1] - t[l - 1])
