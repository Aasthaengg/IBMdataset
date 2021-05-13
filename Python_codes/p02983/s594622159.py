def main():
    mod = 2019
    l,r = map(int,input().split())
    ans = 10**9
    for i in range(l,min(l+2020,r+1)):
        for j in range(i+1,min(l+2020,r+1)):
            ans = min(ans,(i*j)%mod)
    print(ans)
main()