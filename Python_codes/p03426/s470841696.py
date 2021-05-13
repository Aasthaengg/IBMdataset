H, W, D = map(int, input().split())

# W_max = (W)
fields = [0] * (W*H+1)
# 一列にして、保存しておこうか。
for i in range(H):
    rows = list(map(int, input().split()))
    for j,r in enumerate(rows):
        ind = i * W + j
        fields[r] = ind

def calc(l,r):
    indl = fields[l]
    hl = indl // W
    wl = indl % W
    indr = fields[r]
    hr = indr // W
    wr = indr % W
    d = abs(hl-hr) + abs(wl-wr)
    return d

# 累積
x = [[] for i in range(D)]  

for i in range(D):
    acc = 0
    x[i].append(0)
    for j in range(i, W*H+1, D):
        # print(j)
        acc += calc(j-D,j)
        x[i].append(acc)

# print(x)


### query
Q = int(input())
for _ in range(Q):
    L,R = map(int, input().split())
    amari = L%D
    print(x[amari][(R-amari)//D+1]-x[amari][(L-amari)//D+1])   