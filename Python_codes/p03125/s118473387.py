# ABC118 A

def main():
    a, b = map(int, input().split())

    if b % a:
        print(b - a)
    else:
        print(a + b)

if __name__ == '__main__':
    main()