t = input()
s = input()
ans = ""
l = len(s)
for i in range(len(t)-len(s)+1):
    p = t[i:i+l]
    count = 0
    for j in range(l):
        if s[j] == p[j] or p[j] == "?":
            count += 1
        else:
            break
    if count == l:
        ans = t[:i]+s+t[i+l:]
if ans == "":
    print("UNRESTORABLE")
    exit()

for i in range(len(ans)):
    if ans[i] == "?":
        print("a", end="")
    else:
        print(ans[i], end="")
print()
