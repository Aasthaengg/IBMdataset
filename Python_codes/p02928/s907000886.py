def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    mod = 10**9+7
    loop = [0 for i in range(n)]
    t = [0 for i in range(n)]
    for i in range(n-1):
        for j in range(i,n):
            if a[i]>a[j]:
                loop[i] += 1
    for i in range(n):
        for j in range(n):
            if a[i]>a[j]:
                t[i] += 1
    s = (sum(loop) * k) % mod
    s += (sum(t) * (k * (k-1) //2)) % mod
    print(s%mod)

if __name__ == "__main__":
    main()
