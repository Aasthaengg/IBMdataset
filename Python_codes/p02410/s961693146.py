def my_dot(lhs, rhs):
    return [sum(a[i][j] * b[j][0] for j in range(len(rhs))) for i in range(len(lhs))]


if __name__ == '__main__':
    from sys import stdin

    n, m = (int(n) for n in stdin.readline().rstrip().split())

    a = []
    for cnt in range(n):
        a.append([int(n) for n in stdin.readline().rstrip().split()])

    b = []
    for cnt in range(m):
        b.append([int(n) for n in stdin.readline().rstrip().split()])

    c = my_dot(a, b)

    for cn in c:
        print(int(cn))

