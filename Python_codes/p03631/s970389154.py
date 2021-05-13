
url = "https://atcoder.jp//contests/abc070/tasks/abc070_a"

def main():
    x = input()
    if x == ''.join(reversed(x)):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
