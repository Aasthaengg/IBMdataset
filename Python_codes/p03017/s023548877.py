import sys
input = sys.stdin.readline
N, A, B, C, D = map(int, input().split())
S = list(input())

# A < B < D, A < B < C
# A < D, B < C の間に # が2マス連続にあったらNo
# さらに D < C なら すぬけくんとふぬけくんが入れ替わる必要がある。
# すなわち3マス連続...が続いている必要がある(#が2マス連続ないことも注意)

left = A

if C < D:
    right = D
else:
    right = C
    idx = []
    for i in range(B - 2, D - 1):
        if S[i] == '.' and S[i + 1] == '.' and S[i + 2] == '.':
            idx.append(i)
    if not idx:
        print('No')
        exit()
    # print('idx', idx)
    # print('idx', S[idx[0]:idx[0] + 10])
# print('N, A, B, C, D', N, A, B, C, D)
T = S[left - 1:right + 1]
# print('T', T)
for i in range(len(T) - 1):
    if T[i] == '#' and T[i + 1] == '#':
        print('No')
        exit()

print('Yes')
