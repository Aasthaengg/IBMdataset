def main():
    A,B = [int(x) for x in input().split()]
    ans = 0
    p = 1
    while p<B:
        p += A-1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()