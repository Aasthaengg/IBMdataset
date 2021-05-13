def main():
    n, c = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(c)]
    C = [list(map(int, input().split())) for _ in range(n)]
    ans = [None]*3
    for k in range(3):
        costs = []
        for nc in range(c):
            cost = 0
            for i in range(n):
                s = (i+k)%3
                ci = C[i]
                for j in range(2-s, n, 3):
                    color = ci[j]-1
                    cost += D[color][nc]
            costs.append(cost)
        ans[k] = list(sorted({index:cost for index, cost in enumerate(costs)}.items(), key=lambda x: x[1]))[:3]
    out = 10**12
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if len(set([ans[0][i][0], ans[1][j][0], ans[2][k][0]])) == 3:
                    out = min(out, ans[0][i][1]+ans[1][j][1]+ans[2][k][1])
    print(out)
            
    
if __name__ == "__main__":
    main()