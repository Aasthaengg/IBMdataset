# B - Counting Roads
def main():
    import collections


    n, m = map(int, input().split())
    cnt = []

    for _ in range(m):
        temp = list(input().split())
        cnt += temp
    else:
        ans = collections.Counter(cnt)
        for i in range(1, n+1):
            print(ans[str(i)])


if __name__ ==  "__main__":
    main()