def main():

    count = dict()
    for _ in range(3):
        a, b = map(int, input().split())
        count[a] = count.get(a, 0) + 1
        count[b] = count.get(b, 0) + 1
    if sorted(count.values()) == [1, 1, 2, 2]:
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())