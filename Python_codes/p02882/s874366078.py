a,b,x = map(int,input().split())
import math
# 0025~
# xがa*a*bの半分仮想で内科で場合分け.片側が常に限界まで水があるので
# 右へ右へと傾けていくことを考えている
maxL = a*a*b
# 半分より大きい場合．すなわち左側の水線がどんどん落ちていく場合，
rest = maxL -x
if rest <= maxL / 2:
    # 半分の容量に対してどれだけ減ったかを調べる
    dropped = (rest / (maxL/2)) * b
    # 傾けた角度は，dropped, a, の辺を持った直角三角形の角度tan-1(dropped/a)となる.
    theta = math.atan(dropped/a) / math.pi * 180.0
    print(abs(theta))
    exit()

# 半分より小さい場合，すなわち水線が底面の左から落ちていく場合
# 作られる削ってくる三角形
#rest = (maxL/2)-x
#dropped = rest /(maxL/2)
# ああ逆でいいのか
h = a * (x/(maxL/2))
theta2 = math.atan(h/b)/math.pi * 180.0
theta1 = math.atan(b/a)/math.pi * 180.0
# 更に傾けた角度は，(180-theta1) - theta2
print(theta1 + (90-theta1)-theta2)





