s = input()
n = len(s)

s = s.replace("BC","X")
s += "DD"
nn = len(s)

alen = 0
ans = 0
for i in range(nn):
    if s[i] == "A":
        alen += 1
    elif s[i] == "X":
        ans += alen
    else:
        alen = 0
        
print(ans)