import sys
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

S = LI2()

a = 10*S[0]+S[1]
b = 10*S[2]+S[3]

if 1 <= a <= 12 and 1 <= b <= 12:
    print('AMBIGUOUS')
elif not 1 <= a <= 12:
    if 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')
else:
    print('MMYY')

