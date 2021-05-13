s = input()

ind = []
for i in range(len(s)):
    if s[i] == "B":
        ind.append(i)

cnt = s.count("B")

target = list(range(len(s)))[-cnt:]

ans = 0
for t, i in zip(target, ind):
    ans += t-i
print(ans)