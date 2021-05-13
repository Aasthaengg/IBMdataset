import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(str(input()))
length = len(S)

abc_cnt = 0
a_cnt = 0
ans = 0
for i in range(length):
    s = S[i]
    if s=='A':
        if abc_cnt!=1:
            a_cnt = 0
        a_cnt += 1
        abc_cnt = 1
    elif s=='B':
        if abc_cnt==1:
            abc_cnt += 1
        else:
            a_cnt = 0
            abc_cnt = 0
    else:
        if abc_cnt==2:
            abc_cnt = 1
            ans += a_cnt
        else:
            a_cnt = 0
            abc_cnt = 0
print(ans)