def main():
    n, m = map(int, input().split())

    cities = [0 for _ in range(n)]

    for i in range(m):
        a, b = map(int, input().split())

        cities[a - 1] += 1
        cities[b - 1] += 1
    
    for bridges in cities:
        print(bridges)

if __name__ == '__main__':
    main()