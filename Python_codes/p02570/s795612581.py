# Dは距離　Tは制限時間　速度はS
Information_Lists = input().split()
#.split("文字列")で、文字列ごとに分けることができる。"文字列"を入れないとスペースで分けられる。
D = int(Information_Lists[0])
T = int(Information_Lists[1])
S = int(Information_Lists[2])
if D > T * S:
    print("No")
else:
    print("Yes")