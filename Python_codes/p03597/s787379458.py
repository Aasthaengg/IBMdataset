from sys import stdin

def main():
    n = int(stdin.readline())
    w = int(stdin.readline())

    print(n ** 2 - w)

if __name__ == '__main__':
    main()