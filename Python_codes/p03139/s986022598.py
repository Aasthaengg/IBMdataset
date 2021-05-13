def main():
    N,A,B = map(int,input().split())
    print(min(A,B),end=" ")
    print(max(0,(A+B)-N))
if __name__ == '__main__':
    main()