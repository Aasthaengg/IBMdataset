def main():
    s = input()
    counts = [0]

    for c in s:
        if c == 'S':
            counts.append(0)
        if c == 'R':
            counts[-1] += 1

    print(max(counts))


if __name__ == '__main__':
    main()
