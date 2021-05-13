import sys
read = sys.stdin.read
def main():
    n, c = map(int, input().split())
    d = {e: [0] * (c + 1) for e in range(100001)}
    d1 = [0] * 100001
    m = map(int, read().split())
    stc = zip(m, m, m)
    for s, t, c in stc:
        if d[s][c]:
            d1[s - 1] -= 1
            d1[s] += 1
        else:
            d[s][c] = 1
        if d[t][c]:
            d1[t - 1] -= 1
            d1[t] += 1
        else:
            d[t][c] = 1
        d1[s - 1] += 1
        d1[t] -= 1

    cur = 0
    r = 0
    for i1 in range(100001):
        cur += d1[i1]
        r = max(r, cur)
    print(r)

if __name__ == '__main__':
    main()
