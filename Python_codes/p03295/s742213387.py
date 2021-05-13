import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    dislike = []
    for _ in range(M):
        a, b = map(int, input().split())
        dislike.append((a, b))

    """
    aについて昇順に貪欲法を考えて破綻しました。。。
    （その後aの昇順にdpすることも考えたけど同じく行き詰まり）
    bについての昇順なら貪欲法がうまく回ります。
    「貪欲法はあらゆる変数に対して考えるべし」ということなのか？
    """
    dislike.sort(key=lambda x: x[1])
    cnt = 0
    last = -1 # 最後に落とした橋
    for a, b in dislike:
        if a <= last: continue
        cnt += 1
        last = b - 1
    print(cnt)



if __name__ == "__main__":
    main()
