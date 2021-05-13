import math

def main():
    A, B, C, D = map(int, input().split())
    lcm = C * D // math.gcd(C, D)
    C_div = B // C - (A - 1) // C
    D_div = B // D - (A - 1) // D
    C_D_div = B // lcm - (A - 1) //lcm
    print(B - A + 1 - C_div - D_div + C_D_div)


if __name__ == '__main__':
    main()
