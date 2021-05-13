def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    a_ = int(input())
    if a_ != 0:
        print(-1)
        return True
    for n in range(N-1):
        a = int(input())
        if a - a_ > 1:
            print(-1)
            return True
        if a - a_ == 1:
            ans += 1
            a_ = a
        else:
            ans += a
            a_ = a
    print(ans)

if __name__ == '__main__':
    main()