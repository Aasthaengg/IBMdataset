import math

N,A,B = map(int, input().split())

H = [int(input()) for _ in range(N)]
H.sort(reverse=True)

# mid回の攻撃で全撃破できるか確認。
hi = math.ceil(H[0] / B)
lo = 1


while hi - lo > 1:
    can_defeat_all_enemies = True
    mid = (hi+lo) // 2
    cnt_extra_attack = 0

    for i in range(N):
        if H[i] > mid * B:
            cnt_extra_attack += math.ceil((H[i] - mid * B) / (A - B))
        # 降順に並べてあるので、あるモンスターで追加攻撃が必要なければそれ以降も必要ない
        else:
            break
    
    # mid以下しか追加攻撃が必要ないので倒しきれる
    if cnt_extra_attack <= mid:
        hi = mid
    else:
        lo = mid

print(hi)
