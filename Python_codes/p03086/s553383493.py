import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()
A = ['A','T','C','G']
a = 0
ans = 0
for i in range(len(S)):
    if S[i] in A:
        a += 1
    else:
        ans = max(ans,a)
        a = 0

ans = max(ans,a)

print(ans)
