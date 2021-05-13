
url = "https://atcoder.jp//contests/abc073/tasks/abc073_b"

def main():
    n = int(input())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))

    count = 0
    for li in t:
        count += (li[1] - li[0]) + 1
    print(count)


if __name__ == '__main__':
    main()
