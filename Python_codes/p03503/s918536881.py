n = int(input())
F = []
# for _ in range(n):
#     f = list(map(int, input().split()))
#     # print(f)
#     F.append([\
#         [f[0],f[1]],\
#         [f[2],f[3]],\
#         [f[4],f[5]],\
#         [f[6],f[7]],\
#         [f[8],f[9]]\
#     ])

for _ in range(n):
    f = list(map(int, input().split()))
    F.append(f)

# print(*F,sep='\n')

P = []
for _ in range(n):
    p = list(map(int, input().split()))
    P.append(p)

# print(*P,sep='\n')

def c(i, open_my_shop):
    ret = 0
    for j in range(10):
        if open_my_shop>>j & 1: #open my shop
            if F[i][j]: # open your shop
                ret += 1
    return ret

ans = -10*10000000*10
# for i in range(1, 1<<10): # [0~1,1~1] 10bit
#     s = 0
#     for j in range(10): # open time zone
#         if i>>j & 1: # my shop (j+1) open
#             for k in range(n): # your shop
#                 ck = c(k, i)
#                 s += P[k][ck]
#     ans = max(ans ,s)

for i in range(1, 1<<10): # [0~1,1~1] 10bit
    s = 0
    for j in range(n): # your shop
        cj = c(j, i)
        s += P[j][cj]
    ans = max(ans ,s)

print(ans)
