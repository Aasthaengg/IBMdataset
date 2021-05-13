import fractions

def main():
    a, b = map(str, input().split())
    a = int(a)
    b = fractions.Fraction(b)
    print(int(a*b))

if __name__ == "__main__":
    main()
