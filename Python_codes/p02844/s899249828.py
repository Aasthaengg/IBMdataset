def main():
    N = int(input())
    S = input()[::-1]
    digits_1 = [0] * 10
    digits_2 = [[0 for _ in range(10)] for _ in range(10)]
    digits_3 = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)]
    for i, d in enumerate(S):
        d = int(d)
        for d1 in range(10):
            for d2 in range(10):
                if digits_2[d2][d1] == 1:
                    digits_3[d][d2][d1] = 1
        for d1 in range(10):
            if digits_1[d1] == 1:
                digits_2[d][d1] = 1
        digits_1[d] = 1
    ans = 0
    for d3 in range(10):
        for d2 in range(10):
            for d1 in range(10):
                ans += digits_3[d3][d2][d1]
    print(ans)


if __name__ == '__main__':
    main()