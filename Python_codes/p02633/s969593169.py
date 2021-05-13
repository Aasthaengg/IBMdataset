from fractions import gcd

def main():
    x = int(input())
    a = gcd(360,x)
    print(360//a)

if __name__ == "__main__":
    main()