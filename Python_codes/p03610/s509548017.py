import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
ans = ''
for i in range(0,len(S),2):
    ans += S[i]

print(ans)
