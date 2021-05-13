s = input()
t = input()
s = sorted(s)
t = sorted(t)
S = ""
T = ""
for i in range(len(s)):
    S += s[i]
for i in range(len(t)):
    T += t[len(t) - 1 - i]
print("Yes" if T > S else "No")
