def main():
    num = int(input())
    CONST = 1000000007
    lis = [1] * 2100
    for i in range(3):
        lis[i] = 0
    for i in range(3,2020):
        for j in range(3,i):
            lis[i] += lis[i-j]
            lis[i] %= CONST
    print(lis[num])
if __name__ == '__main__':
    main()
