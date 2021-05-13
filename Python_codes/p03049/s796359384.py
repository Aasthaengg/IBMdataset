n = int(input())
ans = 0
sb = []
fa = []

def ABCount(s):
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == "A" and s[i+1] == "B":
            cnt += 1
    return cnt

for i in range(n):
    s = input()
    ans += ABCount(s)
    if s[0] == "B":
        sb.append(i)
    if s[-1] == "A":
        fa.append(i)

if len(sb) == len(fa) and len(sb) > 0:
    sb.sort()
    fa.sort()
    f = False
    for i in range(len(sb)):
        if not sb[i] == fa[i]:
            f = True
            break
    if f:
        ans += len(sb)
    else:
        ans += len(sb)-1
else:
    ans += min(len(sb),len(fa))

print(ans)
