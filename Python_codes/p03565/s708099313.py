s = input()
t = input()
c = -1
for i in range(len(s)-len(t)+1):
    sw = 1
    for j in range(len(t)):
        if s[i+j] == "?":
            pass
        elif s[i+j] == t[j]:
            pass
        else:
            sw = 0
            break
    if sw == 1:
        c = i
if c == -1:
    ans = "UNRESTORABLE"
else:
    a = []
    i = 0
    j = 0
    while i < len(s):
        if c <= i < c+len(t):
            a.append(t[j])
            j += 1
        elif s[i] != "?":
            a.append(s[i])
        else:
            a.append("a")
        i += 1
    ans = "".join(a)
print(ans)