def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        c = 0
        while i<k:
            i = i*2
            c += 1
        ans += 1/n * (1/2)**c
    print(ans)

if __name__ == "__main__":
    main()
