N = int(input())
f = []
for i in range(N):
    F = map(str, input().split())
    f.append("0B" + ''.join(F))
P = [list(map(int, input().split())) for i in range(N)]

ans = -float("inf")
for bit in range(1, 2 ** 10):
    profit = 0  
    for i in range(N):    
        c = bin( bit & int(f[i], 0) )
        index = c.count('1')
        profit += P[i][index]
    ans= max(ans, profit)

print(ans)