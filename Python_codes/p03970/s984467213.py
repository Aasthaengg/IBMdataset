s = input()
ans = 0
for i, j in zip(s, "CODEFESTIVAL2016"):
    if i != j:
        ans += 1
print(ans)
