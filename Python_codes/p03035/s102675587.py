def main():
    a, b = [int(x) for x in input().split()]
    if a > 12:
        print(b)
    elif 6 <= a <= 12:
        print(int(b/2))
    else:
        print(0)
main()