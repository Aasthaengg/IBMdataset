s = input()
t = input()
ss = s+s
NEXT = [[-1]*(len(s)+1) for _ in range(26)]
cur = [-1]*26
for i in range(len(ss)):
    char = ord(ss[i])-97
    if cur[char] < len(s):
        for j in range(cur[char],min(i,len(s))):
            NEXT[char][j+1] = i
            cur[char] = i
ans = 0
tmp = -1
for i in range(len(t)):
    char = ord(t[i])-97
    if NEXT[char][tmp+1] == -1:
        print(-1)
        exit()
    ans += NEXT[char][tmp+1]-tmp
    tmp = NEXT[char][tmp+1]
    if tmp >= len(s):
        tmp -= len(s)
print(ans)
