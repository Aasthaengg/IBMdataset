def main():
    n = int(input())
    a = list(map(int,input().split()))
    res = 0.0
    for i in a:
        res += 1/i
    print(1/res)

if __name__ == '__main__':
    main()
