import sys

a, b, k = map(int, input().split())

for i in range(a, min(b, a + k)):
    print(i)

 # 左側の幅だけで全部網羅する場合
if b < a + k:
    print(b)
    sys.exit()

 # ベン図みたいにかぶってる時
for i in range(max( a + k, b + 1 - k ), b + 1):
    print(i)