def main():
    n = int(input())
    a = set()
    for i in range(n):
        m = input()
        if m in a:
            a.remove(m)
        else:
            a.add(m)
    print(len(a))


if __name__ == "__main__":
    main()
