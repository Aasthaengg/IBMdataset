def main():
    X,Y = map(int,input().split())
    if X%Y==0:
        print(-1)
    else:
        for i in range(1,10**8):
            if (X*i)%Y != 0:
                print(X*i)
                exit()
if __name__ == "__main__":
    main()