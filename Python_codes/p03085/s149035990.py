# A - Double Helix
# A：アデニン T：チミン G：グアニン C：シトシン
# 対になる組み合わせ  A-T  G-C

# 標準入力
base = input()
# print(base)

# 条件分岐し、結果を answer に代入
if base == 'A':
    # print('T')
    answer = 'T'
elif base == 'T':
    # print('A')
    answer = 'A'
elif base == 'G':
    # print('C')
    answer = 'C'
elif base == 'C':
    # print('G')
    answer = 'G'

# 結果の出力
print(answer)
