# coding: utf-8

def main():
    N = int(input())
    ans = ':('

    for i in range(50001):
        if int(i * 1.08) == N:
            ans = i
            break

    print(ans)


if __name__ == "__main__":
    main()
