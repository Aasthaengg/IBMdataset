s = input()
w = int(input())
n = len(s)

res = []
m = n // w
for i in range(m + 1):
    if w*i >= n: continue
    res.append(s[w*i])

print(''.join(res))