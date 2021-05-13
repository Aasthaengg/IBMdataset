def agc014_b():
    n, m = map(int, input().split())
    deg = [0]*n
    for _ in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        deg[a] += 1
        deg[b] += 1
    for k in deg:
        if k%2 == 1:
            return print('NO')
    print('YES')

if __name__ == '__main__':
    agc014_b()