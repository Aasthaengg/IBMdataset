# returns : Nのd進数表記
def base_n_num(N, d):
    p = 1
    ans = []
    if N == 0:
        return [0]
    while N != 0:
        if N % (d**p) == 0:
            ans.append(0)
        else:
            ans.append(1)
            N -= (d**(p-1))
        p += 1
        if N == 0:
            break
    return reversed(ans)

def solve():
    n = int(input())

    # 下の桁から求める
    ans = base_n_num(n, -2)
    print(''.join(list(map(str, ans))))

solve()
