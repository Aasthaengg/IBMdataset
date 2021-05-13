def main():

    a,b,k = map(int,input().split())
    next = 'a'
    for i in range(k):
        if next == 'a':
            if a % 2 == 1:
                a -= 1
            a = a // 2
            b += a
            next = 'b'
        else:
            if b % 2 == 1:
                b -= 1
            b = b // 2
            a += b
            next = 'a'

    print(a,b)



if __name__ == '__main__':
    main()
