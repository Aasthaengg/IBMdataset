def main():
    while True:
        try:
            a,b = map(int,input().split())
            c = a*b
            if a < b:
                a,b = b,a
            while a%b != 0:
                a,b = b,a%b
            print(b,c//b)
        except EOFError:
            exit()

if __name__ == '__main__':
    main()