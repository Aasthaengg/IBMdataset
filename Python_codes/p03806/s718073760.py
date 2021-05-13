MOD = 10 ** 9 + 7
INF = 10  ** 7
def main():
    n,a,b = map(int,input().split())
    m = n//2
    Chemical = [tuple(map(int,input().split())) for _ in range(n)]
    Chemical1 = Chemical[:m]
    Chemical2 = Chemical[m:]
    Sum1 = [[INF] * 405 for _ in range(405)]
    Sum2 = [[INF] * 405 for _ in range(405)]
    for bit in range(1<<m):
        cost,v1,v2 = 0,0,0
        for i in range(m):
            if (bit>>i)&1:
                d,e,f = Chemical1[i]
                v1 += d
                v2 += e
                cost += f
        Sum1[v1][v2] = min(Sum1[v1][v2],cost)
    
    for bit in range(1<<(n - m)):
        cost,v1,v2 = 0,0,0
        for i in range(n - m):
            if (bit>>i)&1:
                d,e,f = Chemical2[i]
                v1 += d
                v2 += e
                cost += f
        Sum2[v1][v2] = min(Sum2[v1][v2],cost)
    
    ans = INF
    for i in range(405):
        for j in range(405):
            if Sum1[i][j] != INF:
                C = Sum1[i][j]
                k = max((i + a - 1)//a,(j + b - 1)//b,1)
                while k * a - i < 405 and k*b - j < 405:
                    if Sum2[k*a - i][k*b - j] != INF:
                        ans = min(ans,Sum2[k*a - i][k*b - j] + C)
                    k += 1
    print(ans if ans != INF else -1)
if __name__ == '__main__':
    main()