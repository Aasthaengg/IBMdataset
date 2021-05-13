def main():
    s = input()
    count = {"a": 0, "b": 0, "c": 0}
    for ss in s:
        count[ss] += 1
    count = list(count.values())
    count.sort()
    print("YES" if count[-1] - count[0] <= 1 else "NO")


if __name__ == '__main__':
    main()

