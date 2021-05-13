# tenka1-2017-beginnerB - Different Distribution
def main():
    N, *AB = map(int, open(0).read().split())
    A = max(zip(*[iter(AB)] * 2))
    ans = sum(A)
    print(ans)


if __name__ == "__main__":
    main()