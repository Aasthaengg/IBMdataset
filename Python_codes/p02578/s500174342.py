def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if x[i] > x[i+1]:
            ans += x[i]-x[i+1]
            x[i+1] = x[i]
    print(ans)


main()
