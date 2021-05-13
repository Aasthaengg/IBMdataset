def main():
    n, m = map(int,(input().split()))
    if m==1 and n == 1:
        print(1)
    elif n <= 2 and m <= 2:
        print(0)
    elif n>2 and m>2:
        print((n-2)*(m-2))
    elif n>2:
        if m == 2:
            print(0)
        else:
            print(n-2)
    elif m>2:
        if n == 2:
            print(0)
        else:
            print(m-2)
    

    

        


if __name__ == "__main__":
    main()