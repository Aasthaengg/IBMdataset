from sys import stdin
input = stdin.buffer.readline

def main():
    n, m = map(int, input().split())

    yp = [(0, 0)] * m
    for i in range(m):
        p, y = map(int, input().split())
        yp[i] = (y, p-1, i)

    yp.sort(key=lambda x: x[0])

    ans = [('', '')] * m
    cnt = [1] * n
    for y, p, i in yp:
        ans[i] = (str(p+1), str(cnt[p]))
        cnt[p] += 1

    for i, j in ans:
        print('0' * (6 - len(i)) + i + '0' * (6 - len(j)) + j)

main()