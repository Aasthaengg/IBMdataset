if __name__ == '__main__':
    n = int(input())
    k = int(input())
    a = [int(i) for i in input().split()]

    ans = 0

    for i in a:
        ans += min ( abs(i),abs(k-i) )
    print(ans*2)

