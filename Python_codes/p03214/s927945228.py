from statistics import mean
def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = mean(a)
    x = 10**6
    ans = -1
    for i in reversed(range(n)):
        if abs(a[i] - m) <= x:
            ans = i
            x = abs(a[i] - m)
    print(ans)

if __name__ == "__main__":
    main()
