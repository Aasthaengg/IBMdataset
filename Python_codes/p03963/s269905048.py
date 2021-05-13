def main():
    N,K = map(int,input().split())
    if N == 1:
        print(str(K))
    else:
        ans = (K-1)**(N-1)*K
        print(str(ans))





if __name__ == '__main__':
    main()