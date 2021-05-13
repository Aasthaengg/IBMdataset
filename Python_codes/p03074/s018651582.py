from itertools import accumulate


def main():
    n, k = map(int, input().split())
    s = list(input())
    l = []
    if s[0] == "0":
        l.append(["1", 0])
    l.append([s[0], 1])
    for i in range(1, n):
        if s[i] == l[-1][0]:
            l[-1][1] += 1
        else:
            l.append([s[i], 1])
    if s[-1] == "0":
        l.append(["1", 0])
    count = []
    for standing, c in l:
        count.append(c)
    count = list(accumulate(count))
    count = [0] + count
    answer = 0
    for i in range(0, len(count), 2):
        j = i + 2 * k + 1
        if j >= len(count):
            j = len(count) - 1
        answer = max(answer, count[j] - count[i])
    print(answer)


if __name__ == '__main__':
    main()

