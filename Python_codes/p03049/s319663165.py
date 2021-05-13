n = int(input())
s = [[] for _ in range(n)]

for i in range(n):
    s[i] = input()
comb = [[0]*2 for i in range(2)]
    
al = 0
be = 0
ans = 0
for i in range(n):
    m = len(s[i])
    for j in range(m-1):
        if s[i][j] == "A" and s[i][j+1] == "B":
            ans += 1
    if s[i][0] == "B" and s[i][-1] == "A":
        comb[1][1] += 1
    elif s[i][0] == "B" and s[i][-1] != "A":
        comb[0][1] += 1
    elif s[i][0] != "B" and s[i][-1] == "A":
        comb[1][0] += 1
    else:
        comb[0][0] += 1
        
if comb[0][1] == 0 and comb[1][0] == 0:
    ans += max(0,comb[1][1] - 1)
elif comb[0][1] != 0 and comb[1][0] == 0:
    ans += comb[1][1]
elif comb[0][1] == 0 and comb[1][0] != 0:
    ans += comb[1][1]
else:
    ans += (comb[1][1] + 1 + min(comb[1][0]-1,comb[0][1]-1))
    
print(ans)
