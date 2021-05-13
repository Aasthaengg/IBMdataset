def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    odd = len([a for a in A if a & 1])
    even = N - odd
    if odd & 1:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()
