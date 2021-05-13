s = input()
n = len(s)
p = []
flag = False
for i in range(n-1):
    if flag:
        flag = False
        continue 
    if s[i] == "B" and s[i+1] == "C":
        flag = True
        p.append("#")
    elif s[i] == "A":
        p.append(s[i])
    else:
        p.append("!")

nowa = 0
ans = 0
for i in range(len(p)):
    if p[i] == "A":
        nowa += 1
    elif p[i] == "#":
        ans += nowa
    elif p[i] == "!":
        nowa = 0
print(ans)