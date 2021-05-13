def main():
    N = int(input())
    ls = [[int(x) for x in input().split()] for _ in range(N)]
    ls = sorted(ls,key=lambda x:-x[0])
    print(sum(ls[0]))
if __name__ == "__main__":
    main()