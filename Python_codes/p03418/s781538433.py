from fractions import gcd

def NK():
    return map(int,input().split())

def main():
    n,k = NK()
    ans = 0
    for i in range(1,n+1):
        ans += (n//i)*max((i-k),0) + max(n%i-max((k-1),0),0)
    print(ans)

if __name__ == "__main__":
    main()