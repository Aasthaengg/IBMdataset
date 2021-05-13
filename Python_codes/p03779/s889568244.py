# でました 「最大（この問題の場合は毎回右に移動する）で移動したとき、今より前の地点は、『今まで動いたiのいずれかを省く』ことで到達してたことにできる」というやつ（わかりにくい
# なので、xに到達した時点でそれまでの値はすべて実現可能という感じ

from math import ceil
x = int(input())
tmp = 0
for i in range(x + 1):
    tmp += i
    if tmp >= x:
        print(i)
        exit()

print("うんち！")