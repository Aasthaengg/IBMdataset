def main():
    A, B = map(int, input().split())

    next = A + B
    if next >= 24:
        next -= 24

    print(next)
main()