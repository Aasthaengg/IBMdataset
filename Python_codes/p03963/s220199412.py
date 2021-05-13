import sys
input = sys.stdin.readline

def main():
    N, K = [int(x) for x in input().split()]

    print(K * (K - 1) ** (N - 1))

    

if __name__ == '__main__':
    main()


