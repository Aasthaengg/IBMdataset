def main():
    K,X = list(map(int,input().split()))

    price = 500 * K
    if(price >= X):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
