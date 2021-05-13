# 累積和の考え方
#   listに積み重ねた数値を出しておくことで特定範囲の数値を求める時間を短縮する
#   例：ABBBBAABBBBAB があるときに(l,r)にAがいくつ含まれるかを求める場合は以下のように(1長い)listを作る
#      BBABBBAABBBBAA
#      000111123333345
#   このリストの文字列のr-lで出せる(3,7)ならstr[7]-str[3]を出すと3-1で2となる

n, q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

# 累積和のリストを作成
cumsum = [0]*(n+1)
for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        cumsum[i+1]+=cumsum[i]+1
    else:
        cumsum[i+1]=cumsum[i]

# 012345   index
# 123456   input
# ACACAC   s
# 0011223  cumsum
for left, right in lr:
    print(cumsum[right]-cumsum[left])