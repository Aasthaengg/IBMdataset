import collections
n = int(input())
s = input()
l = s.count("W")
r = s.count("E")
ans = 0
keep = r
minn = keep
if s[0] == "E":
    ans = 1
for i in range(1, n):
    if s[i - 1:i + 1] == "WW":
        keep += 1
    elif s[i - 1:i + 1] == "WE":
        keep += 0
    elif s[i - 1:i + 1] == "EW":
        keep += 0
    elif s[i - 1:i + 1] == "EE":
        keep -= 1
    if minn > keep:
        minn = keep
print([minn, minn - 1][ans])
