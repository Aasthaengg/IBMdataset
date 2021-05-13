def main():
    n = int(input())
    k = int(input())
    r = 1
    for i in range(n):
        r = min(r * 2, r + k)

    print(r)

if __name__ == '__main__':
    main()
