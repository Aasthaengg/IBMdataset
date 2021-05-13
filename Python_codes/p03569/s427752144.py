s = list(input())
swox = []
xnum = []

count = 0
for i in range(len(s)):
    if s[i] != 'x':
        swox.append(s[i])
        xnum.append(count)
        count = 0
    if s[i] == 'x':
        count += 1

xnum.append(count)

for i in range(len(swox)//2):
    if swox[i] != swox[-i-1]:
        print(-1)
        exit()

if len(swox) == 0 or sum(xnum) == 0:
    print(0)
else:
    ans = 0
    for i in range(len(xnum)//2):
        ans += abs(xnum[i]-xnum[-i-1])
    print(ans)