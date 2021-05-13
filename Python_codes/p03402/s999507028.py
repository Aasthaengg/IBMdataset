#ABC092-D Grid Components
"""
問題：
100*100以下のグリッドを作成し、
白・黒に色を塗る時、白の連結成分の個数をwに、
黒の連結成分をbとしたものを出力せよ
解法：
まずグリッドは100*100としてよい。
上50行を黒、下50行を白で塗る(w,b>=1)
上50行100列のうち、w-1個だけ斜めに配置する
同じように下50行100列もb-1個だけ斜めに配置
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
w,b = map(int,readline().split())
H,W = 100,100
print(H,W)
ans = [["."]*W for _ in range(H//2)]
ans += [["#"]*W for _ in range(H//2)]

i,j = 0,0
res = b-1
while True:
    if res == 0:
        break
    if j+2 >= W:
        i += 2
        j = 0 if even(i) else 1
        ans[i][j] = "#"
        res -= 1
    else:
        j += 2
        ans[i][j] = "#"
        res -= 1
i,j = 51,0
res = w-1      
while True:
    if res == 0:
        break
    if j+2 >= W:
        i += 2
        j = 0 if even(i) else 1
        ans[i][j] = "."
        res -= 1
    else:
        j += 2
        ans[i][j] = "."
        res -= 1
for i in ans:
    print("".join(i))