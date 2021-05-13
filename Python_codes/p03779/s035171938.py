#3問目
#いけるまでいってはみ出したら戻る
X = int(input())
position = 0
count = 0
while position < X:
    count += 1
    position += count
if position == X:
    print(count)
else:
    print(count )