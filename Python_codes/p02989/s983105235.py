def main():
    n = int(input())
    inlis = list(map(int,input().split()))
    inlis.sort()

    left = inlis[int(n//2)-1]
    right = inlis[int(n//2)]

    print(right-left)

if __name__ == "__main__":
    main()
