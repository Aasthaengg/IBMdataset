import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,A,B,C,D = MI()
S = ['#'] + LS2()

for i in range(A,C):
    if S[i] == S[i+1] == '#':
        print('No')
        exit()
for i in range(B,D):
    if S[i] == S[i+1] == '#':
        print('No')
        exit()

if C < D:  # 追い越ししなくてよい
    print('Yes')
else:  # 追い越し必要
    for i in range(B,D+1):
        if S[i-1] == S[i] == S[i+1] == '.':
            print('Yes')
            break
    else:
        print('No')
