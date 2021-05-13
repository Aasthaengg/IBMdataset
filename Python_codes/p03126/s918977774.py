def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        tmp = [int(i) for i in input().split()]
        a.append(tmp)
    l = [0 for i in range(m)]
    for i in range(n):
        k = a[i][0]
        for j in range(1,k+1):
            l[a[i][j]-1] +=1
    ans = 0
    for i in range(m):
        if l[i] == n:
            ans += 1
    print(ans)

main()