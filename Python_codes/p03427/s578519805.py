def main():
    import sys
    input = sys.stdin.readline
    N = input().strip()
    L = len(N)
    N = int(N)
    s = ''
    ans = 0
    for _ in range(L):
        t = 9
        while int(str(t) + s) > N:
            t -= 1
        s = str(t) + s
        ans += t
    print(ans)    

if __name__ == '__main__':
    main()