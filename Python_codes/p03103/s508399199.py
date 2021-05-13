def main():
    N,M = map(int, input().split())
    AB = []
    for i in range(N):
        A,B =  map(int, input().split())
        AB.append((A,B))
    AB.sort()
    coin = 0

    for i in range(N):
        temp = min(M,AB[i][1])
        coin += temp * AB[i][0]
        M -= temp
        if M==0:
            break


    print(coin)


if __name__ == '__main__':
    main()

