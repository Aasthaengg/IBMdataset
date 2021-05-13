ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))


def main():
    n = ii()

    a = []
    direct = [[True for i in range(n)]for j in range(n)]

    for i in range(n):
        a.append(li())


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][j] > a[i][k] + a[k][j]:
                    print(-1)
                    return
                
                if i==k or k == j:
                    continue
                if a[i][j] == a[i][k] + a[k][j]:
                    direct[i][j] = False
    
    ans = 0
    for i in range(n):
        for j in range(n):
            if direct[i][j]:
                ans += a[i][j]
    print(ans//2)


main()