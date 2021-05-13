# vim: fileencoding=utf-8


def main():
    n = int(input())
    max_k = n // 7
    max_d = n // 4
    for i in range(max_k + 1):
        for j in range(max_d + 1):
            if i * 7 + j * 4 == n:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
