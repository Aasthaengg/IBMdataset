# Aさんは a[m] 地点、Bさんは b[m] 地点、Cさんは c [m] 地点にいます。
# 二人の人間は、距離が d [m] 以内のとき直接会話が出来ます。
# AさんとCさんが直接的、あるいは間接的に会話ができるか判定してください。
# ただしAさんとCさんが間接的に会話ができるとは、AさんとBさんが直接会話でき、かつBさんとCさんが直接会話できることを指します。

# 標準入力から a, b, c, d を取得する
a, b, c, d = map(int, input().split())

# 会話ができる（直接or間接）かを判定し、結果を出力する
result = 'No'

if abs(a - c) <= d: # 直接会話可能
    result = 'Yes'
elif (abs(a - b) <= d) and (abs(b - c) <= d):
    result = 'Yes'

print(result)
