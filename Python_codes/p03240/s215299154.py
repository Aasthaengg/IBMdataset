import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 全探索


def check(pos):
    # 2つ目以降の条件について検討
    flg = True
    for x, y, h in xyh[1:]:
        if h != max(pos[2] - abs(x - pos[0]) - abs(y - pos[1]), 0):
            flg = False
            break
    return flg


def main(xyh):
    # Aは頂点候補のリスト
    A = []
    # 1つ目の条件から高さを求める
    # 1つ目の条件の高さが0だと、頂点の高さが分からないのでソート
    xyh.sort(key=lambda x: x[2], reverse=True)
    x, y, h = xyh[0]
    for i in range(101):
        for j in range(101):
            H = h + abs(x - i) + abs(y - j)
            A.append([i, j, H])
    # 全ての頂点候補について条件に合うかチェック
    for pos in A:
        if check(pos):
            break
    top = pos
    return top


n = int(readline())
xyh = [list(map(int, readline().split())) for _ in range(n)]

top = main(xyh)
print(*top)
