
url = "https://atcoder.jp//contests/abc127/tasks/abc127_c"

def main():
    n, m = list(map(int, input().split()))
    l, r = 0, 999999
    for i in range(m):
        a,b = list(map(int, input().split()))
        l = a if a > l else l
        r = b if b < r else r
    ans = r - l
    print(ans + 1) if ans >= 0 else print(0)


if __name__ == '__main__':
    main()
