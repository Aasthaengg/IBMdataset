from collections import defaultdict

def main():
    d = defaultdict(int)
    n, m = [int(i) for i in input().split()]
    py = {}

    for i in range(m):
        p, y = [int(i) for i in input().split()]
        py[i] = (p, y)

    res = [''] * m
    for v in sorted(py.items(), key=lambda x:x[1]):
        d[v[1][0]] += 1
        res[v[0]] = str(v[1][0]).zfill(6) + str(d[v[1][0]]).zfill(6)
    for r in res:
        print(r)

if __name__ == '__main__':
    main()

