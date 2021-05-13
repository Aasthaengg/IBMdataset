def main():
    import math
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    hakobu = min(a, b, c, d, e)
    kaisuu = math.ceil( n / hakobu)

    print(kaisuu + 4)



if __name__ == "__main__":
    main()