def main():
    s=int(input())
    a=s//(10**9)
    b=s%(10**9)
    if s!=10**18:
        print(0)
        print(0)
        print(10**9)
        print(1)
        print(10**9-b)
        print(a+1)
    else:
        print(0)
        print(0)
        print(0)
        print(10**9)
        print(10**9)
        print(0)

if __name__ == "__main__":
    main()