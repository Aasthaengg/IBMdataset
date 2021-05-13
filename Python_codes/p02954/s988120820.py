import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
length = len(S)
ans = [0]*length
now = 'R'
for i in range(length):
    s = S[i]
    if s=='R':
        now = 'R'
        continue
    if s=='L':
        if now=='R':
            now = 'odd'
            plus = i
            ans[plus] += 1
        elif now=='odd':
            now = 'even'
            ans[plus-1]+=1
        else:
            now = 'odd'
            ans[plus]+=1
now = 'L'
for i in range(length-1, -1, -1):
    s = S[i]
    if s=='L':
        now = 'L'
        continue
    if s=='R':
        if now=='L':
            now = 'odd'
            plus = i
            ans[plus] += 1
        elif now=='odd':
            now = 'even'
            ans[plus+1]+=1
        else:
            now = 'odd'
            ans[plus]+=1
print(*ans)