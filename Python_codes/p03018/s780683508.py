s = input()
l = len(s)
s += "0"
ans = 0
a_cnt = 0
skip = False
for i in range(l):
    if skip:
        skip = False
        continue
    if s[i] == "A":
        a_cnt += 1
    elif s[i] == "B" and s[i+1] == "C":
        ans += a_cnt
        skip = True
    else:
        a_cnt = 0

print(ans)
