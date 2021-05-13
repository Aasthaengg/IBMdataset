def main():
    MOD = 10**9 + 7
    n, k = map(int, input().split())
    ans = 0
    for x in range(k, n+2):
        ans +=  (n+2)*(n+1)//2 - (n-x+2)*(n-x+1)//2 - (x+1)*x//2 + 1
        ans %= MOD
    print(ans)

if __name__ == "__main__":
    main()