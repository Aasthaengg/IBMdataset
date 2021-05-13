def main():
    n = int(input())
    ps = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if ps[i] == i+1:
            if ps[i] == n:
                ps[i-1], ps[i] = ps[i], ps[i-1]
            else:
                ps[i], ps[i+1] = ps[i+1], ps[i]
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
