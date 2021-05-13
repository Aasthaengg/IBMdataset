# tenka1-2017-beginnerB - Different Distribution
def main():
    N, *AB = map(int, open(0).read().split())
    A = [(i, j) for i, j in zip(*[iter(AB)] * 2)]
    A.sort()
    ans = sum(A[-1])
    print(ans)


if __name__ == "__main__":
    main()