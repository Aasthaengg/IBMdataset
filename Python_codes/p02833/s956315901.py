def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    n = int(input())
    if n%2 == 1:
        print(0)
        exit(0)
    
    def count(k, n):
        now = k
        cnt = 0
        while now <= n:
            cnt += n//now
            now *= k
        return cnt

    n //= 2
    cnt2 = n
    cnt2 += count(2, n)
    cnt5 = count(5, n)
    ans = min(cnt2, cnt5)
    print(ans)

if __name__ == '__main__':
    main()