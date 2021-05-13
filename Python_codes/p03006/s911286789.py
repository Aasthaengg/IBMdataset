from collections import Counter

if __name__ == "__main__":
    n = int(input())
    pos = list()
    for i in range(n):
        pos.append(list(map(int, input().split())))

    # まず1個のボールを最初選びそこから次のボールを選んだときの距離をp,qとして
    # それぞれの組み合わせの最汎値を求める
    dist = list()
    for i in range(n):
        for j in range(n):
            if i != j:
                tmp = (pos[j][0] - pos[i][0], pos[j][1]-pos[i][1])
                dist.append(tmp)

    # most_comon(n)とすると、最も出現回数が多い順からn要素を抽出する
    pq = Counter(dist).most_common(1)

    print(n - pq[0][1] if n != 1 else 1)
