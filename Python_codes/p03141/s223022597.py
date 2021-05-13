def main():
    dishes = int(input())
    aoki_happiness = []
    difference = []
    for i in range(dishes):
        t, a = map(int, input().split())
        aoki_happiness.append(a)
        difference.append(t + a)
    difference.sort(reverse=True)
    answer = -sum(aoki_happiness)
    for i in range(dishes):
        if i % 2 == 0:
            answer += difference[i]
    print(answer)


if __name__ == '__main__':
    main()

