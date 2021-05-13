def main():
    # n = int(input())
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if abs(a-b)>k or abs(a-c)>k or abs(a-d)>k or abs(a-e)>k or abs(b-c)>k or abs(b-d)>k or abs(b-e)>k or abs(c-d)>k or abs(c-e)>k or abs(d-e)>k:
        print(":(")
    else:
        print("Yay!")


if __name__ == '__main__':
    main()
