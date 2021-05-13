def main():
    n,a,b=map(int,input().split())
    if a > b:
        print(0)
    elif n < 2 and a != b:
        print(0)
    else:
        print(b*(n-2)-a*(n-2)+1)

if __name__ == "__main__":
    main()