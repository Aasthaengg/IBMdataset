# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in li:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 1 and even == 0:
        print("YES")
        return
    if odd % 2 == 1:
        print("NO")
        return
    if odd % 2 == 0 and (even + odd // 2) == 0:
        print("NO")
        return
    print("YES")


if __name__ == "__main__":
    main()
