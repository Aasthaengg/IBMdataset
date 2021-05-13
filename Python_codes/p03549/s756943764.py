def main():
    N, M = map(int, input().split())
    
    total = 0
    for i in range(1, 10 ** 5):
        # x = ((i + 1) * 1900) * ((1/2) ** (i + 1))

        # x = (1900 + 1900 + 800) * i
        # y = x * ( ( (3/4) ** (i-1) ) * (1/4) )
        # total += y
        # print(x, y)

        x = (1900 * M + 100 * (N - M)) * i
        prob = (1/2) ** M
        y = x * ( ( (1-prob) ** (i-1) ) * prob )
        total += y
        # print(':', prob, x, y, total)

    print(round(total))

if __name__ == "__main__":
    main()