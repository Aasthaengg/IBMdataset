
url = "https://atcoder.jp//contests/abc134/tasks/abc134_d"

def main():
    n = int(input())
    a = [0]
    a.extend(list(map(int, input().split())))
    balls = [0]*(n+1)
    b = {}
    for i in range(n, 0, -1):
        ball = 0
        for j in range(i, n+1, i):
            ball += balls[j]
        if ball % 2 != a[i]:
            b[i] = 1
            balls[i] = 1
    if len(b) == 0:
        print(0)
        exit()
    else:
        print(len(b))
    ks = sorted(b.items(), key=lambda x:x[0])
    for k in ks:
        print(k[0], end=" ")


if __name__ == '__main__':
    main()
