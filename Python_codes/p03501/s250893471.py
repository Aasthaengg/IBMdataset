def main():
    input_string = list(map(int,input().split()))
    N = input_string[0]
    A = input_string[1]
    B = input_string[2]

    price1 = A*N
    price2 = B

    print(min(price1,price2))

main()
