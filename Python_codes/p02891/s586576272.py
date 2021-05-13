import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

s = ns()
k = ni()
cnt = 1
li = []
prev = '@'
for c in s:
    if c == '@':
        cnt = 1
        prev = c
        continue
    elif prev == c:
        cnt += 1
    else:
        li.append(cnt)
        cnt = 1
        prev = c
else:
    li.append(cnt)
li = li[1:]

ans_ele = 0
ans = 0
if len(set(s)) == 1:
    ans = len(s) * k // 2
elif s[0] == s[-1] and (li[0] + li[-1]) % 2 == 0:
#elif s[0] == s[-1] and li[0] == 1 and li[-1] == 1 :
    for e in li:
        if e >= 2:
            ans_ele += e // 2
    ans = ans_ele * k + k - 1
else:
    for e in li:
        if e >= 2:
            ans_ele += e // 2
    ans = ans_ele * k
print(ans)

""" same
1 ~ 1 :  + (k - 1)
2 ~ 1 : X
1 ~ 2 : X
2 ~ 2 : X
 and len(li) != 1
"""