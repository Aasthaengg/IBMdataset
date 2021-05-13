
url = "https://atcoder.jp//contests/abc096/tasks/abc096_a"

def main():
    m, d = list(map(int, input().split()))
    ans = m
    if m > d:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
