class Rectangle:
    def __init__(self, a, b):
        S = a * b
        L = a + a + b + b
        print(str(S) + ' ' + str(L))

if __name__ == "__main__":

    a, b = map(int, raw_input().split())
    rc = Rectangle(a, b)