def main():
    A = list(input())
    B = list(input())
    if A == B:
        print("EQUAL")
    elif len(A) > len(B):
        print("GREATER")
    elif len(A) < len(B):
        print("LESS")
    else:
        for a, b in zip(A, B):
            if a > b:
                print("GREATER")
                break
            elif a < b:
                print("LESS")
                break


if __name__ == '__main__':
    main()
