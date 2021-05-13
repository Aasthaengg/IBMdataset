
def resolve():
    # WAの数はACを出した問題だけ数える
    N, M = map(int, input().split())

    ans = [False]*N
    WA = [0]*N
    ac, wa_tot = 0, 0
    for _ in range(M):
        q, s = input().split()
        q = int(q)-1
        if ans[q]:
            continue
        if s == "AC":
            ans[q] = True
            ac += 1
            wa_tot += WA[q]
        if s == "WA":
            WA[q] += 1

    print(ac, wa_tot)

if __name__ == "__main__":
    resolve()