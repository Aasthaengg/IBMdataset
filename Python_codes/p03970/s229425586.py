s = input()
t = "CODEFESTIVAL2016"
ans = 0
for i,x in enumerate(s):
    if x != t[i]:
        ans += 1
print(ans)