
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    lim = 1e18
    ans = 1
    if 0 in a:
        print(0)
        return
    for i in a:
        ans *= i
        if ans >lim:
            print(-1)
            return
    print(ans)

if __name__ == "__main__":
    main()