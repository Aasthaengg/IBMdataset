s = input()
s2 = "CODEFESTIVAL2016"
ans = 0
for x, y in zip(s, s2):
    if x != y:
        ans += 1
print(ans)
