def main():
    n = int(input())
    X = [int(x) for x in input().split()]
    min_x = min(X)
    max_x = max(X)
    min_e = 10**6
    for i in range(min_x, max_x+1):
        error = 0
        for x in X:
            error += (x-i) ** 2
        min_e = min(min_e, error)
    print(min_e)

if __name__ == '__main__':
    main()