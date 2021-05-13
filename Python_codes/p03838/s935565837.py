def main():
    x, y = map(int, input().split())
    answer = 0
    if abs(x) != abs(y):
        answer += abs(abs(x) - abs(y))
    if (x < 0 and y < x < 0) or (0 < y < x):
        answer += 2
    elif x * y < 0 or (0 < x and y == 0) or (x == 0 and y < 0):
        answer += 1
    print(answer)


if __name__ == '__main__':
    main()

