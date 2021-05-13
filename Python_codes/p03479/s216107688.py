def main():
    X,Y = map(int,input().split(" "))
    A = int(X)
    ans = 1
    while A <= Y:
        A *= 2
        if A <= Y:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()