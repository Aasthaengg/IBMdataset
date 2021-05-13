import sys

N = int(input())
line_data = input()
data = list(map(lambda x: int(x), line_data.split(' ')))

if N == 0:
    if data[0] == 1:
        print(1)
    else:
        print(-1)
    sys.exit(0)

tmp_sum = sum(data)
tmp_data = []
for i in data:
    tmp_sum -= i
    tmp_data.append(tmp_sum)

num = 1
prev_leaf = 1
for i, d in enumerate(data[:-1]):
    tmp = (prev_leaf - d) * 2
    top = tmp_data[i]
    if tmp <= 0:
        num = -1
        break
    if tmp < top:
        prev_leaf = tmp
    else:
        prev_leaf = top
    num += prev_leaf
else:
    if prev_leaf != data[-1]:
        num = -1

print(num)
