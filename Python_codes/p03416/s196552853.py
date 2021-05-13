def main():
    a, b = map(int, input().split())

    res = 0

    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            res += 1
    
    print(res)

if __name__ == '__main__':
    main()