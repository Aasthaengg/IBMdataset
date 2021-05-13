n,a,b,c,d = map(int,input().split())
S = list(input())

flg = 1
for i in range(a-1,c-2):
    if S[i:i+2] == ['#','#']:
        flg *= 0

for i in range(b-1,d-2):
    if S[i:i+2] == ['#','#']:
        flg *= 0

if c>d:
    flg2 = 0
    for i in range(b-1,d):
        if S[i-1:i+2] == ['.','.','.']:
            flg2 = 1
    flg *= flg2

if flg == 0:
    print('No')
else:
    print('Yes')