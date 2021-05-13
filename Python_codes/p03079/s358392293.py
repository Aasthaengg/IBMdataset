import sys

# 標準入力を読み込み，float型へ変換
s = input().split()
f = [ float(x) for x in s]

# 正三角形の条件
if (f[0]==f[1] and f[1]==f[2]):
    print('Yes')
else:
    print('No')