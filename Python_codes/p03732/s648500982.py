import sys
from itertools import accumulate as acc

def main():
    N, W = map(int, input().split())
    V = [[] for _ in '1234']

    w, v = map(int, input().split())
    w0 = w
    V[0].append(v)
    for e in sys.stdin:
        w, v = map(int, e.split())
        V[w - w0].append(v)

    for i in range(4):
        V[i] = [0] + list(acc(sorted(V[i], reverse=True)))

    ans = 0
    a, b, c, d = map(len, V)
    for i in range(a):
        wi = w0 * i
        if wi > W:
            break
        vi = V[0][i]
        for j in range(b):
            wj = wi + (w0 + 1) * j
            if wj > W:
                break
            vj = vi + V[1][j]
            for k in range(c):
                wk = wj + (w0 + 2) * k
                if wk > W:
                    break
                vk = vj + V[2][k]

                l = min((W - wk) // (w0 + 3), d - 1)
                v = vk + V[3][l]
                ans = max(ans, v)
    print(ans)

if __name__ == '__main__':
    main()