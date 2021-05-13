S = [1 if x=="W" else 0 for x in input()]

groups = []
tmp = 0
zeros = 0
for n in S:
    if n == 1:
        if zeros != 0:#直前まで０だったとき
            groups.append(zeros)
            zeros = 0#リセット
        tmp += 1
    elif n == 0:
        if tmp != 0:#直前まで１だったとき
            groups.append(tmp)
            tmp = 0#リセット
        zeros -= 1

#終端の処理
if tmp != 0:
    groups.append(tmp)
if zeros != 0:
    groups.append(zeros)
    
print(len(groups)-1)