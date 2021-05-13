n = int(input())
s = input()
ans = 0

lchrs = [0]*26
rchrs = [0]*26
flag = [False]*26
for c in s:
    lchrs[ord(c)-ord("a")] += 1

for c in s:
    i = ord(c)-ord("a")
    lchrs[i] -= 1
    rchrs[i] += 1
    if lchrs[i] and rchrs[i]:
        flag[i] = True
    else:
        flag[i] = False
    ans = max(ans, len([_ for _ in flag if _]))
print(ans)
