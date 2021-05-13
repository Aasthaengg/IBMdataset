s = [i == "W" for i in list(input())]
n = len(s)
w = []
for i in range(n):
    if s[i]:
        w.append(i)
ans = 0
for i in range(len(w)):
    ans += w[i]-i
print(ans)