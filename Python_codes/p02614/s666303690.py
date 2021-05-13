h, w, k = map(int,input().split())
grid = [list(input()) for _ in range(h)]
ans = 0
# 全行、全列のパターンを全探索
for h_red in range(2**h):
    for w_red in range(2**w):
        
        cnt = 0
        # 前段の2つのfor文で、全パターンについて探索するので、
        # この後の2つのfor文で、パターン毎の#の数をカウントする
        for i in range(h):
            for j in range(w):
                
                # この課題で、一番大事なロジックはここである。
                # ビット演算子>>右シフトと論理積&を組み合わせている
                # h_redやw_redは10進数であるが2進数の場合におけるi、jだけ右にシフトさせる
                # このi、jは10進数扱いであることがややこしい
                # i、jが一周するときに、h_red、w_redをなめているところがポイント
                if (h_red>>i)&1 == 0 and (w_red>>j)&1 == 0:
                    if grid[i][j] == '#':
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)