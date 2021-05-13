def main():
    # n = int(input())
    # h, w, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())
    if b < a:
        b = a + a - b
    if (b+w*t) - (a+v*t) <= 0:
        print("YES")
    else:
        print("NO")



if __name__ == '__main__':
    main()
