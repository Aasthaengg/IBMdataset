def main():
    import math
    s = int(input())
    a = d = math.ceil(math.sqrt(s))
    b, c = 1, a*d-s
    print(0, 0, a, b, c, d)

if __name__ == "__main__":
    main()
