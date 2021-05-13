import math

def main():
    X1, Y1, X2, Y2 = map(float, input().split())

    dist = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
    print(dist)

main()