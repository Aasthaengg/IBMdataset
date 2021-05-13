def main():
    n,k = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t.sort()
    print(sum(t) - sum(t[:n-k]))

if __name__ == '__main__':
    main()
