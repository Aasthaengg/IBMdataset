def main():
    a, b, x = map(int, input().split())

    result = False
    for i in range(0, b+1):
        if a + i == x:
            result = True
            break
    
    if result:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
