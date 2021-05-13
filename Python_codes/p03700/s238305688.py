
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# A = [ int(input()) for _ in range(N) ]
##############################

N, A, B = map(int, input().split())
H = []
for i in range(N):
    h = int(input())
    H.append(h)


def solve(bomb):
    count = 0
    for i in range(N):
        remain = H[i] - (B*bomb)
        # まだ残ってる場合、中心爆発分で追加ダメージが必要なのでカウントする
        if remain > 0:
            additional_damage = (A-B)
            c = -(-remain // additional_damage)
            count += c

    if count <= bomb:
        return True
    else:
        return False


# leftは条件を満たす値、rightは満たさない値
def meguru(left, right):
    while abs(left - right) > 1:
        mid = (left + right) // 2;

        if (solve(mid)):
            left = mid
        else:
            right = mid;

    return left


# 問題を「k回の爆発でクリアできるか」に置き換えれば、めぐる式二分探索が使える
print(meguru(max(H), 0))