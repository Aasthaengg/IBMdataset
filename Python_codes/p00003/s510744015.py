def main():
    """ ????????? """
    num = int(input())
    for i in range(num):
        m = list(map(int,input().split()))
        m.sort()
        a = (m[0] ** 2) + (m[1] ** 2)
        b = (m[2] ** 2)
        if a == b:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()