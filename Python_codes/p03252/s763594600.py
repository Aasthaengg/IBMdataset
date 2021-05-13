s = input()
t = input()
n = len(s)
jisho1 = {}
jisho2 = {}


def ng():
    print("No")
    exit()


for i in range(n):
    if s[i] in jisho1:
        if jisho1[s[i]] != t[i]:
            ng()
    else:
        jisho1[s[i]] = t[i]
    if t[i] in jisho2:
        if jisho2[t[i]] != s[i]:
            ng()
    else:
        jisho2[t[i]] = s[i]
print("Yes")

