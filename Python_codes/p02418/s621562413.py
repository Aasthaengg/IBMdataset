s = input()
p = input()
Ans = False
cnt = 0

for i in range(len(s)):
    for j in range(len(p)):
        if i + j >= len(s):
            i = -j
        if s[i + j] != p[j]:
            break
        cnt += 1
    if cnt == len(p):
        Ans = True
        break
    cnt = 0

if Ans:
    print('Yes')
else:
    print('No')