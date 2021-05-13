s = input()
k = int(input())
res = set()

for i in range(len(s)):
    for j in range(i + 1, i + 1 + k):
        subs = s[i: j]
        res.add(subs)

res = sorted(list(res))
print(res[k - 1])
