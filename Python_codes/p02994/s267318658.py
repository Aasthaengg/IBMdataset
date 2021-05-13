def main():
    N,L = map(int, input().split())
    eat = 10**6
    apples = 0
    for i in range(N):
        apples += i+L
        eat = min(eat,abs(i+L))
    if apples < 0:
        eat *= -1

    print(apples-eat)


if __name__ == '__main__':
    main()

