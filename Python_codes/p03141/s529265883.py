def main():
    n = int(input())
    answer = 0
    dish = []
    for _ in range(n):
        a, b = map(int, input().split())
        dish.append(a + b)
        answer -= b
    dish.sort(reverse=True)
    for i in range(0, n, 2):
        answer += dish[i]
    print(answer)


if __name__ == '__main__':
    main()

