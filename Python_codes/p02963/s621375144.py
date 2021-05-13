def f(x1, y1, x2, y2):
    return abs(x1*y2 - x2*y1)

def main():
    S = int(input())
    d = pow(10, 9)
    X1, Y1 = 0, 0
    X2, Y2 = d, 1
    X3 = (d - S%d)%d
    Y3 = (S + X3) // d
    print(X1, Y1, X2, Y2, X3, Y3)
    #print(f(X2, Y2, X3, Y3))

if __name__ == "__main__":
    main()
