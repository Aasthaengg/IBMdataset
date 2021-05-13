# from sys import stdin
# input = stdin.readline
(R,C,K) = map(int, input().split())
rcv = [list(map(int, input().split())) for _ in range(K)]
 
grids = [[0]*C for _ in range(R)]
 
for r,c,v in rcv:
    grids[r-1][c-1] = v
 
dp = [0] * C

for r in range(R):
#     print(dp)
    ndp = [0] * C
    elm = [0] * 4
    for c in range(C):
        elm[0] = max(elm[0], dp[c])
        value = grids[r][c]
        if value:
            nelm = [0] * 4
            nelm[0] = elm[0]
#             print(f'{value=}')
#             print(f'{ elm=}')
#             print(f'{nelm=}')
            for i in range(3)[::-1]:
                nelm[i + 1] = max(elm[i + 1], elm[i] + value)
#             print(f'{value=}')
#             print(f'{ elm=}')
#             print(f'{nelm=}')
            elm = nelm
        ndp[c] = max(elm)
    dp = ndp
 

print(dp[-1])