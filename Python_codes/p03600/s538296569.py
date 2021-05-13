def main():
    from sys import stdin
    input = stdin.readline

    n = int(input())
    a = [[int(i) for i in input().split()] for _ in range(n)]

    ans = 0
    tf = [[True] * n for _ in range(n)]
    # Warshall-Floyd algorithm
    for k in range(n):
        for i in range(n-1):
            if i == k:
                continue
            for j in range(i, n):
                if j == k:
                    continue
                elif a[i][j] > a[i][k] + a[k][j]:
                    print(-1)
                    exit()
                elif a[i][j] == a[i][k] + a[k][j] and tf[i][j]:
                    ans -= a[i][j]
                    tf[i][j] = False
    
    ans += sum([sum(i) for i in a]) // 2
    print(ans)

main()