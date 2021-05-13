import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()

if not (S.count('C') == 1 and S[0] == 'A' and S[1] != 'C' and S[-1] != 'C'):
    print('WA')
    exit()
else:
    for i in range(1,len(S)):
        if not (S[i] == 'C' or S[i].islower()):
            print('WA')
            exit()
print('AC')
