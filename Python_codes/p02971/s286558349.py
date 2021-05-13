
url = "https://atcoder.jp//contests/abc134/tasks/abc134_c"

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    sort_a = sorted(a, reverse=True)
    for v in a:
        if sort_a[0] == v:
            print(sort_a[1])
        else:
            print(sort_a[0])

if __name__ == '__main__':
    main()
