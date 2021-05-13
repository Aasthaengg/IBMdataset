s = list(input())
t = ["A", "K", "I", "H", "A", "B", "A", "R", "A"]


if s[-1] != "A":
    s = s + ["A"]
for i in range(len(t)):
    if len(s) <= i: break
    if t[i] != s[i] and t[i] != "A":
        break
    if t[i] != s[i] and t[i] == "A":
        s.insert(i, "A")

if s == t:
    print("YES")
else:
    print("NO")