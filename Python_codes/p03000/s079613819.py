def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    sum = 0
    for idx, i in enumerate(l):
        sum += i
        if sum > x:
            print(idx + 1)
            break
    else:
        print(n + 1)

if __name__ == '__main__':
    main()