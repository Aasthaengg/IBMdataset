def main():
    N,K = map(int,input().split())
    print(N-(N//K)*K)
if __name__ == '__main__':
    main()