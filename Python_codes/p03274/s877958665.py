def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 10**18
    for i in range(n-k+1):
        ans = min([ans, abs(a[i])+abs(a[i]-a[i+k-1]),\
                abs(a[i+k-1])+abs(a[i]-a[i+k-1])])
    print(ans)
        

    
if __name__ == '__main__':
    main()