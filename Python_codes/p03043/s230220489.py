import math

def main():
    N, K = map(int, input().split())
    prob = 0
    for i in range(1, N+1):
        if K / i <= 1:
            prob += 1
        else:
            coin = math.ceil(math.log2(K / i))
            prob += 0.5 ** coin
    print(prob / N)


if __name__ == '__main__':
    main()
