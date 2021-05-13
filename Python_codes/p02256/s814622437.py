def main():
    a, b = tuple(map(int,input().split()))
    if a < b:
        (a, b) = (b, a)
        # a > b となるように並べ替え
    print(gcd(a, b))

def gcd(x, y):    
    
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

if __name__ == '__main__':
    main()

