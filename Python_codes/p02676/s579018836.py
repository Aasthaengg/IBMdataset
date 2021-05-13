'''
問題：
    英小文字からなる文字列 S があります。

    S の長さが K 以下であれば、Sをそのまま出力してください。
    S の長さが K を上回っているならば、先頭 K 文字だけを切り出し、
    末尾に ... を付加して出力してください。
'''

'''
制約：
    K は 1 以上 100 以下の整数
    S は英小文字からなる文字列
    S の長さは 1 以上 100 以下
'''

# 標準入力からK, S を取得する
k = int(input())
s = str(input())

result = ""
if len(s) <= k:
    result = s
else:
    for i in range(0, k):
        result += s[i]
    result += "..."

print(result)
