def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    k,t = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = max(a[0]-1-sum(a[1:]),0)
    print(ans)

    
if __name__ == '__main__':
    main()