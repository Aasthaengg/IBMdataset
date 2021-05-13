def main():
    n = int(input())
    c = 0
    
    if n % 2 == 1:
        print(0)
        return 
    
    i = 10
    x, _ = divmod(n, i)
    while x:
        c += x
        i *= 5
        x, _ = divmod(n, i)

    print(c)


if __name__ == '__main__':
    main()
