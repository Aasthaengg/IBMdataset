s = list(input())
k = int(input())
ans = []
now = s[0]
cou = 0
if len(s) == 1:
    print(k//2)
    exit()

for i in range(len(s)):
    if now == s[i]:
        cou += 1
    elif now != s[i]:
        ans.append(cou)
        cou = 1
        now = s[i]
if cou > 0:
    ans.append(cou)
if ans[0] == len(s):
    print((ans[0]*k)//2)
    exit()
    
p = 0
for i in ans:
    p += (i//2)*k

if s[0] == s[-1]:
    p -= (ans[0]//2 + ans[-1]//2)*(k-1)
    p += ((ans[0]+ans[-1])//2)*(k-1)

print(p)