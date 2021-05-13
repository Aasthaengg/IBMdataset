N = int(input())
town = {}

for i in range(N):  # 地名をキーとした辞書に、[店番号、点数]を付加する
    place, score = input().split()
    tmp = [i+1, int(score)]
    if place in town:
        town[place].append(tmp)
    else:
        town[place] = [tmp]

index = list(town.keys())
index.sort()

for _ in index:
    tmp = town[_]
    tmp = sorted(tmp, reverse=True, key=lambda x: x[1])
    for num in tmp:
        print(num[0])
