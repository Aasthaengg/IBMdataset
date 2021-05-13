import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
cntb =0
cntw = s.count('.')
ans =cntw
for i in range(len(s)):
    if s[i] == '#':
        cntb +=1
    else:
        cntw -=1
    ans = min(ans,cntb+cntw)
print(ans)