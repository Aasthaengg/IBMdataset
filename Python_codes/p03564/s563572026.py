def main():
    N = int(input())
    K = int(input())
    answer = 1
    for _ in range(N):
        if answer > K:
            answer += K
        else:
            answer *= 2
    print(answer)


if __name__ == '__main__':
    main()

