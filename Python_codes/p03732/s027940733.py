import sys
input = sys.stdin.readline

def main():
    N, W = map(int, input().split())
    wv = [list(map(int, input().split())) for i in range(N)]

    base_w = wv[0][0]
    dic = {wv[0][0]:[], wv[0][0]+1:[], wv[0][0]+2:[], wv[0][0]+3:[]}
    for i in range(N):
        w, v = wv[i]
        dic[w].append(v)
    
    # python3.7.2だと奇跡的に辞書型が宣言順になってたけど，
    # python3.4.3だと順序が保証されないのでちゃんとソートしないとだめ!
    wv = sorted(list(dic.items()))
    tmp = [None for i in range(4)]
    for i in range(4):
        num, l = wv[i]
        l = sorted(l, reverse=True)
        for j in range(1, len(l)):
            l[j] += l[j-1]
        tmp[i] = [0] + l

    # for i in range(4):
    #     print(tmp[i][:10])

    ans = 0
    for i in range(len(tmp[0])):
        for j in range(len(tmp[1])):
            for k in range(len(tmp[2])):
                for l in range(len(tmp[3])):
                    weight = base_w * i + (base_w + 1) * j + (base_w + 2) * k + (base_w + 3) * l
                    if weight <= W:
                        val = tmp[0][i] + tmp[1][j] + tmp[2][k] + tmp[3][l]
                        if ans < val:
                            ans = val
    print(ans)

if __name__ == "__main__":
    main()