from itertools import accumulate

N, C  = map(int, input().split())
x_cw = []   # 時計
x_acw = []  # 反時計
v_cw = []     # 寿司
for i in range(N):
    x,v = map(int, input().split())
    x_cw.append(x)
    v_cw.append(v)
v_acw = v_cw[::-1]
x_acw = [C - x for x in x_cw[::-1]]
x_cw = [0] + x_cw
x_acw = [0] + x_acw
# print(x_cw)
# print(x_acw)
v_cw1 = [v_cw[i]-(x_cw[i+1]-x_cw[i]) for i in range(N)]        # 時計回り折り返さない
v_cw2 = [v_cw[i]-2*(x_cw[i+1]-x_cw[i]) for i in range(N)]     # 時計回り折返しが入るとき
v_acw1 = [v_acw[i]-(x_acw[i+1]-x_acw[i]) for i in range(N)]        # 反時計折り返さない
v_acw2 = [v_acw[i]-2*(x_acw[i+1]-x_acw[i]) for i in range(N)]     # 反時計折返しがはいるとき

acc_cw1 = list(accumulate(v_cw1))
acc_acw1 = list(accumulate(v_acw1))
acc_cw2 = list(accumulate(v_cw2))
acc_acw2 = list(accumulate(v_acw2))

acc_acw1 = acc_acw1[::-1]
acc_cw1 = acc_cw1[::-1]


max_cw2 = []
m = 0
# 右スタート、左バックパターン
for c in acc_cw2:
    m = max(c,m)
    max_cw2.append(m)
ans_cw = acc_acw1[0] #初期値
for i in range(1,N):
    ans_cw = max(ans_cw, max_cw2[i-1]+acc_acw1[i])

# 左スタート、右バックパターン
m = 0
max_acw2 = []
for c in acc_acw2:
    m = max(c, m)
    max_acw2.append(m)
ans_acw = acc_cw1[0] # 初期値 
for i in range(1,N):
    ans_acw = max(ans_acw, max_acw2[i-1]+acc_cw1[i])
ans = max(ans_acw,ans_cw)
print(max(0,ans))
