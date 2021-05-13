# 数直線上にいるAさんとBさんとCさんがトランシーバーで会話をしようとしています。
# Aさんはa[m] 地点、Bさんはb[m] 地点、Cさんはc[m] 地点にいます。
# 二人の人間は、距離がd [m]以内のとき直接会話が出来ます。
# AさんとCさんが直接的、あるいは間接的に会話ができるか判定してください。
# ただしAさんとCさんが間接的に会話ができるとは、AさんとBさんが直接会話でき、
# かつBさんとCさんが直接会話できることを指します。

a,b,c,d = map(int,input().split())

# 絶対値を返す関数：abs(x)
Between_a_to_c = abs( a - c )
Between_a_to_b = abs( a - b )
Between_b_to_c = abs( b - c )

# 条件分岐
if not Between_a_to_c > d:
    print('Yes')
elif not Between_a_to_b > d:
    if not Between_b_to_c > d:
        print('Yes')
    else:
        print('No')
else:
    print('No')
