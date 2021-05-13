import math

def main():
    A, B, C = map(int, input().split())

    c = math.radians(C)
    s = A * B * math.sin(c) / 2
    l = A + B + math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(c))
    h = B * math.sin(c)

    print(s)
    print(l)
    print(h)

main()