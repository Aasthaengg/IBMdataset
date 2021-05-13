def main():
    N = int(input())
    S = list(input().rstrip())
    vals = [0]
    for s in S:
        if s == "I":
            vals.append(vals[-1] + 1)
        else:
            vals.append(vals[-1] - 1)
    print(max(vals))


if __name__ == '__main__':
    main()
