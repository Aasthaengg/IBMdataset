# mathモジュールをインポート
import math

r = input().rstrip()
r = int(r)

# 円周率の近似値
x = math.pi

ans = (2 * r) * x
print(ans)
