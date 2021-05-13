url = "https://atcoder.jp/contests/abc092/tasks/arc093_a"
import copy
def main():
    n = int(input())
    tmp = list(map(int, input().split()))
    ma = [0]
    ma.extend(tmp)
    ma.append(0)
    all_num = 0
    for i in range(len(ma) - 1):
        all_num += abs(ma[i] - ma[i + 1])
    for i in range(1, len(ma) - 1):
        print(all_num - abs(ma[i - 1] - ma[i]) - abs(ma[i] - ma[i + 1]) + abs(abs(ma[i - 1] - ma[i + 1])))


if __name__ == '__main__':
    main()


