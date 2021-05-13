n = int(input())
s = input()
w = [0]*(n + 2)
e = [0]*(n + 2)
ans = 100000000

for i in range(1, n + 1):
    w[i] += w[i - 1]
    e[-i - 1] += e[-i]
    if s[i - 1] == "W":
        w[i] += 1
    if s[-i] == "E":
        e[-i - 1] += 1

for i in range(1, n + 1):
    ref = e[i + 1]
    ref += w[i - 1]
    ans = min(ans, ref)

print(ans)