def main():
    n=int(input())
    a=list(map(int,input().split()))
    print(sum(a)-len(a))

if __name__ == "__main__":
    main()