
def main():
    a,b,c,d = map(int,input().split())

    first_rectangle = a * b
    second_rectangle = c * d

    print(max(first_rectangle,second_rectangle))

if __name__ == '__main__':
    main()
