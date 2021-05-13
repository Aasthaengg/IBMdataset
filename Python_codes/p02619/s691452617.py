def main():
    days = int(input())
    falliness = [int(x) for x in input().split()]
    satisfactions = [0]  # Never use index 0.
    for _ in range(days):
        satisfactions.append([int(x) for x in input().split()])
    types = []
    for _ in range(days):
        types.append(int(input()))

    last = [0] * 26
    sat = 0
    for date, typ in enumerate(types):
        date += 1
        typ -= 1
        last[typ] = date
        sat += satisfactions[date][typ]
        sat -= sum(falliness[i] * (date - last[i]) for i in range(26))
        print(sat)


if __name__ == '__main__':
    main()
