AB, BC, CA = map(int, input().split())

# 直角三角形 ABCがあります。
#  ∠ABC= 90°です。
#  三角形ABCの三辺の長さである |AB|,|BC|,|CA|が与えられるので、直角三角形 ABCの面積を求めて下さい。

i = (AB * BC) // 2
print(i)