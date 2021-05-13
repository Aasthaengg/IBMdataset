#塩基を入力
base = input()
"AとTのペアで出力、CとGのペアで出力"
if base == "A":
    print("T")
elif base == "T":
    print("A")
elif base == "C":
    print("G")
#AでもTでもCでもなければGなのでCを出力
else:
    print("C")