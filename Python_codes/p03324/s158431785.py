def main():
    D, N = map(int, input().split())
    h = 100
    if N == 100:
        print((100**D)*101)
    else:
        print((100 ** D)*N)
main()  