def main():
    ans = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n-1):
        if l[i] == i+1:
            l[i] = l[i+1]
            l[i+1] = i+1
            ans += 1
    if l[n-1] == n:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()