s = input()
n = int(input())
ss = ""
for i in range(0, len(s), n):
    ss += s[i]
print(ss)

