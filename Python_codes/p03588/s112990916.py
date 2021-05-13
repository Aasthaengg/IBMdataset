import collections


def main():
    n = int(input())
    abList = [0] * n
    for i in range(n):
        abList[i] = list(map(int, input().split()))
    abList.sort(key=lambda x: x[0], reverse=True)
    print(sum(abList[0]))


if __name__ == '__main__':
    main()
