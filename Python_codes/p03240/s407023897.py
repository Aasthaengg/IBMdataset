
def resolve():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    X, Y, H = zip(*P)

    # Cx, Cyを固定して式に当てはめる
    # 逆算している形になっている為、情報Hと矛盾してないのが答え
    # h[i]=0になっているものは距離が分からないので、中心の高さを求めるのには使わない。
    for cx in range(101):
        for cy in range(101):
            h = 1
            for i in range(N):
                if H[i] > 0:
                    h = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
            ok = True
            for i in range(N):
                res = max(h - abs(cx - X[i]) - abs(cy - Y[i]), 0)
                if res != H[i]:
                    ok = False
            if ok:
                print(cx, cy, h)
                return


if __name__ == "__main__":
    resolve()
