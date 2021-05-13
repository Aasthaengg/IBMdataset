S = input()
ans = 0
wc = 0
for i in reversed(S):
    if i == "W":
        wc += 1
    else:
        ans += wc
print(ans)
