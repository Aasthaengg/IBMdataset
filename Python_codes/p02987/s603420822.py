import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
if S[0] == S[1] == S[2] == S[3]:
    print('No')
elif S[0] == S[1] and S[2] == S[3]:
    print('Yes')
elif S[0] == S[2] and S[1] == S[3]:
    print('Yes')
elif S[0] == S[3] and S[1] == S[2]:
    print('Yes')
else:
    print('No')
