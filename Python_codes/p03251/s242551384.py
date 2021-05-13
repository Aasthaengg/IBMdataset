
url = "https://atcoder.jp//contests/abc110/tasks/abc110_b"

def main():
    n, m, x, y = list(map(int, input().split()))
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    xs.sort()
    ys.sort()
    if xs[-1] >= ys[0]:
        print('War')
        exit()
    for i in range(xs[-1] + 1, ys[0] + 1):
        if x < i <= y:
            print('No War')
            exit()
    print('War')


if __name__ == '__main__':
    main()
