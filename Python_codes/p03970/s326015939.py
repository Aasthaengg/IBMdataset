s = list(input())
temp = list("CODEFESTIVAL2016")

ans = 0
for i, j in zip(s, temp):
    if i != j:
        ans += 1

print(ans)