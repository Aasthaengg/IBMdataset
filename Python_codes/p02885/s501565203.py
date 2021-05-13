def main():
    A,B = list(map(int,input().split()))

    result = A - B * 2

    if(result >= 0):
        print(result)
    else:
        print(0)

if __name__ == "__main__":
    main()