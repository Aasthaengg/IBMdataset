def main():
    x, y = map(int, input().split())
    print(gcd(x, y))

def gcd(x, y):
    if(x < y):
        x, y = y, x
    while True:
        if(y == 0):
            return x
        else:
            x, y = y, x%y

if __name__ == '__main__':
    main()