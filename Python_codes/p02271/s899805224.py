# -*- coding=utf-8 -*-
import itertools

count = int(input())
_list = list(map(int, input().split(" ")))

count2 = int(input())
_answers = list(map(int, input().split(" ")))

desc = []
checked = False

# answersの数だけloopして取ってくる
for answer in _answers:
    checked = False
    tmp = [i for i in _list if answer >= i]

    # そもそもtmpの中身をsumしてanswer未満ならば強制的にno
    if answer > sum(tmp):
        desc.append("no")

    # itertoolsのコンビネーションを使用して解く
    else:
        for i in range(len(tmp) + 1):
            if checked == True:
                break

            tmp2 = list(itertools.combinations(tmp, i))
            for tmp3 in tmp2:
                if sum(tmp3) == answer:
                    desc.append("yes")
                    checked = True
                    break

        if checked != True:
            desc.append("no")

for i in desc:
    print(i)

