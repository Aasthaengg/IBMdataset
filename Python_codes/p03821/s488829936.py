def main():
    n = int(input())
    ab = [list(map(int,input().split())) for _ in range(n)]
    res = 0
    for a,b in ab[::-1]:
        a += res
        if a%b != 0:
            res += b-a%b
    print(res)

if __name__ == '__main__':
    main()
