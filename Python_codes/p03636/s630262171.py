
url = "https://atcoder.jp//contests/abc069/tasks/abc069_b"

def main():
    st = input()
    ans = st[0] + str(len(st[1:-1])) + st[-1]
    print(ans)


if __name__ == '__main__':
    main()
