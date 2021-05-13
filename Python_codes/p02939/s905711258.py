S = input().strip()
k = 0
l = ""
r = ""
for s in S:
    r += s
    if l == r:
        continue
    l = r
    r = ""
    k += 1
print(k)
