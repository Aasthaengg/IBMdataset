s = input()
n = len(s)
t = input()
m = len(t)

if n < m:
    print("UNRESTORABLE")
    exit()
p = False
for i in reversed(range(n-m+1)):
    flag = True
    for j in range(m):
        if s[i+j] != "?" and s[i+j] != t[j]:
            flag = False
            break
    if flag:
        s = s[:i] + t + s[i+m:]
        p = True
        break

if not p:
    print("UNRESTORABLE")
    exit()
elif p:
    for i in range(n):
        if s[i] == "?":
            s = s[:i] + "a" + s[i+1:]
print(s)