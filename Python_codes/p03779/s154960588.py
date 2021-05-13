def main():
    X = int(input())
    r = 0
    for i in range(X+1):
        r += i
        if r >= X:
            return i
print(main())
