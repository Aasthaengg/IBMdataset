def main():
    n = input()
    t = list(map(int, input().split()))
    t = [1/v for v in t]
    ans = 1/sum(t)
    print(ans)

if __name__ == '__main__':
    main()