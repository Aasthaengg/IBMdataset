def main():
    N,A,B = map(int,input().split())
    if (B-A)%2 == 1:
        print("Borys")
    else:
        print("Alice")

if __name__ == '__main__':
    main()