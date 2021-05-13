import sys
def LS2():
    return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()

if S[5] == '1' or int(S[6]) >= 5:
    print('TBD')
else:
    print('Heisei')