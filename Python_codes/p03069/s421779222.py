n = int(input())
s = list(input())
ans = 10**6
w = [0]
for i in range(n):
    w.append(w[i] + (s[i] == "."))

for i in range(n + 1):
    ans = min(ans, i - w[i] + (w[-1] - w[i]))

print(ans)
