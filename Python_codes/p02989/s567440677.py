
def main():

    N = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    n = N // 2
    print(d[n] - d[n-1])

if __name__ == "__main__":
    main()

