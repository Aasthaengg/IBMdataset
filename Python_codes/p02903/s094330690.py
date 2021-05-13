H,W,A,B = map(int,input().split())
for i in range(B):
    S = []
    for j in range(A):
        S.append('0')
    for j in range(A,W):
        S.append('1')
    print(''.join(S))
for i in range(B,H):
    S = []
    for j in range(A):
        S.append('1')
    for j in range(A,W):
        S.append('0')
    print(''.join(S))