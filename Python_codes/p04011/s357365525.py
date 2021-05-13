def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    total_price = 0

    for i in range(1,N+1):
        if i <= K:
            total_price += X
        else:
            total_price += Y
    
    print(total_price)

main()