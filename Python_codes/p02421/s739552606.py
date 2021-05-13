def main():
    N = int(input())
    Card = tuple(tuple(input().split()) for _ in range(N))

    taro = 0
    hanako = 0
    for c in Card:
        if c[0] > c[1]:
            taro += 3
        elif c[0] < c[1]:
            hanako += 3
        else:
            taro += 1
            hanako += 1

    print(taro, hanako)

main()