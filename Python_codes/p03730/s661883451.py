# B - Choose Integers
def main():
    a, b, c = map(int, input().split())


    for i in range(1, a*b+1):
        if a*i % b == c:
            print('YES')
            exit()
    else:
        print('NO')


if __name__ ==  "__main__":
    main()