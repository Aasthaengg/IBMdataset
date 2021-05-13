s = input()

base = "CODEFESTIVAL2016"
ans = 0
for e1, e2 in zip(s, base):
    if e1 != e2:
        ans += 1

print(ans)
