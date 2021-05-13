def main():
    h, n = map(int, input().split())
    inlis = list(map(int, input().split()))

    total = sum(inlis)
    if h <= total:
        print("Yes")
    else:
        print("No")


    
if __name__ == "__main__":
    main()
