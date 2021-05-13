from bisect import bisect_right
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [v for v in a]
    for i in range(1, n):
        b[i] += b[i-1]
    ans = 0
    for i in range(n):
        target = b[i]
        index = bisect_right(a, 2*target)
        while index < n:
            target = b[index-1]
            j = index-1
            index = bisect_right(a, 2*target)
            if j+1 == index:
                break
        if index == n:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()