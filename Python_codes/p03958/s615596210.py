from bisect import bisect_left
def main():
    k, t = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    pre = -1
    a.sort()
    for _ in range(k):
        x = bisect_left(a, a[t-1])
        if x == pre:
            if t > 1 and a[x-1] > 0:
                x = bisect_left(a, a[x-1])
            else:
                ans += 1
        a[x] -= 1
        pre = x
    print(ans)

if __name__ == "__main__":
    main()
