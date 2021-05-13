def main():
    N,K=  map(int, input().split())
    sum = K
    for i in range(N-1):
        if K-1 !=0:
            sum = sum * (K-1)

    print(sum)


    
if __name__ == '__main__':
    main()
