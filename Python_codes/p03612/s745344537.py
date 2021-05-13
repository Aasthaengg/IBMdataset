def main():
    n = int(input())
    P = list(map(int, input().split()))
    ans = 0
    next = 0
    on = False
    for i in range(n):
        if P[i] == i + 1:
            ans += 1
            if on:
                next += 1
                on = False
            else:
                on = True
        else:
            on = False
    print(ans - next)

if __name__ == '__main__':
    main()
