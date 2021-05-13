import itertools

n = int(input())

#順列のリストを生成
per_list = []
for i in itertools.permutations([x for x in range(1, n + 1)]) :
    per_list.append(i)

#入力されたタプルが何番目にあるか検索
a = []
for j in range(2) :
    y = tuple(map(int, input().split()))
    a.append(per_list.index(y))

print(abs(a[0] - a[1]))