def main():
    N,K=map(int,input().split())
    print(K*(K-1)**(N-1))

main()