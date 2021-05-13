_ = input()
s = input()
ans = 0
c = 0
for i in s:
    c += 1 if i == "I" else -1
    ans = max(ans, c)
print(ans)