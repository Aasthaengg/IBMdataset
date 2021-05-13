def main():
    import bisect
    n = int(input())
    inlis = list(map(int, input().split()))
    inlis.sort()
    ans = 0
    for a in range(n):
        for b in range(a+1, n):
            c = bisect.bisect_left(inlis, inlis[a] + inlis[b])
            ans += c - b - 1
    print(ans)     



if __name__ == "__main__":
    main()
