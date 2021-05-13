def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 3**N
    cnt = len([a for a in A if a % 2 == 0])
    ans -= 2**cnt
    print(ans)


if __name__ == '__main__':
    main()
