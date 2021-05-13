# 数値の取得
thp,tat,ahp,aat = map(int,input().split())

# 勝敗が決まるまでターンをループ
twin = ""
while twin == "":
    # 高橋君のターン
    ahp -= tat
    if ahp <= 0:
        twin = "Yes"
        break
    # 青木君のターン
    thp -= aat
    if thp <= 0:
        twin = "No"
        break
# 結果を出力
print(twin)