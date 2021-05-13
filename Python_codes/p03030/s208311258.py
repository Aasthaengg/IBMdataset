n = int(input())
dat = []
for i in range(n):
    std_in = input().split()
    dat.append([std_in[0], int(std_in[1])])
     
for i, e in enumerate(dat, start=1):
    e[1] = -e[1]  # 点数を降順ソートするために点数をマイナスにする。
    e.append(i)  # ソート前の順序
     
sorted_list = sorted(dat)  # 都市名と点数のマイナス値で昇順ソート
     
for i, s in enumerate(sorted_list):
    # 順序を出力
    print(sorted_list[i][2])
