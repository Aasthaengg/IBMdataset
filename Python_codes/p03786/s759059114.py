def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0 for i in range(n + 1)]
    a.sort()
    ans = n
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    for i in range(1,n):
        if b[i + 1] - b[i] >  2 * b[i]:
            ans = n - i
    print(ans)

main()