def main():
    S = input()
    d = {'0': 0, '1': 0}
    for s in S:
        d[s] += 1
    print(min(d.values()) * 2)


if __name__ == '__main__':
    main()
