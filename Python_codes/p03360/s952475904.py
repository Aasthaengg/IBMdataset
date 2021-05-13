def main():
    ABC = list(map(int, input().split()))
    K = int(input())
    ABC.sort()
    m = ABC.pop()
    mK = m*(2**K)
    ans = sum(ABC) + mK
    print(ans)

if __name__ == "__main__":
    main()
