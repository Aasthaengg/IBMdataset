
url = "https://atcoder.jp//contests/abc094/tasks/abc094_a"

def main():
    t = list(map(int, input().split()))
    for i in range(t[1]):
        tmp = i + t[0]
        if tmp == t[2]:
            print('YES')
            exit()
    print('NO')

if __name__ == '__main__':
    main()
