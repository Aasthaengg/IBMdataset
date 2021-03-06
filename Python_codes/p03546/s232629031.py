#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
#https://dai1741.github.io/maximum-algo-2012/docs/shortest-path/

INF = (2*10**7)*100 + 1234567 #十分大きい値にすること!!!!!!

H,W = map(int, input().split())
c = [[int(e) for e in input().split()] for i in range(10)]

#Warshall–Floydで1に変える魔力を求めておく
for k in range(10):
    for i in range(10):
        for j in range(10):
            if c[i][j] > c[i][k] + c[k][j] and c[i][k]!=INF and c[k][j]!=INF:
                c[i][j] = c[i][k] + c[k][j]

ans = 0
for i in range(H):
    A_row = [int(e) for e in input().split()]
    for A in A_row:
        if A != -1:
            ans += c[A][1]
            
print(ans)