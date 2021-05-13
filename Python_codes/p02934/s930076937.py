def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += 1/a[i]
    print(1/c)

if __name__ == '__main__':
    main()