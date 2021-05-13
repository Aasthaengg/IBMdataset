def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for x in a:
        C = c
        for i in range(m):
            C += x[i]*b[i]
        if C > 0:
            ans += 1
    print(ans)
    
if __name__ == "__main__":
    main()