# 出現回数が最大の文字に統一することが最小値とは限らないので全ての文字列でシミュレーションする

S = input()

ans = 100
for s in S:
    s_split = S.split(s)
    max_len = 0
    for i in range(len(s_split)):
        max_len = max(max_len, len(s_split[i]))
    ans = min(ans, max_len)
print(ans)
