def main():
    s = input()
    k = int(input())
    d = len(s)
    m = set()
    for i in range(d):
        for j in range(1, k + 1):
            m.add(s[i:i + j])

    m = list(m)
    m.sort()
    print(m[k - 1])


if __name__ == '__main__':
    main()
