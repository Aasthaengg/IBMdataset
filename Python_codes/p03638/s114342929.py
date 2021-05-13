H, W = map(int, input().rstrip().split())
N = int(input())
A = list(map(int, input().rstrip().split()))

muki = 1
m = [[-1] * W for _ in range(H)]
yoko = 0
tate = 0
for i, a in enumerate(A):
    for j in range(a):
        m[tate][yoko] = i + 1
        if yoko + muki >= W or yoko + muki < 0:
            muki *= (-1)
            tate += 1
        else:
            yoko += muki
        
for i in range(H):
    print(' '.join(list(map(str, m[i]))))