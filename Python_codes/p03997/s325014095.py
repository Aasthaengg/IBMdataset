def main():
    a = int(input())
    b = int(input())
    h = int(input())

    square = a * h
    triangle = ((b - a) * h) //2
    print(square + triangle)
main()