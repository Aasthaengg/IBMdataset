import sys
sys.setrecursionlimit(10**7)


def test(array, index, last_position, count, min_count):
    # 除去数が多いパターンは破棄する
    if min_count[0] != -1 and count >= min_count[0]:
        return
    if index + 1 == len(array):
        # print("count:{}".format(count))
        min_count[0] = count if min_count[0] == - \
            1 or count < min_count[0] else min_count[0]
        return
    current = array[index]

    # 前のと手がぶつかる場合は取り除く
    if last_position >= current[2]:
        test(array, index + 1, last_position, count + 1, min_count)
    # 前のとぶつからない場合は取り除かないパターンも
    else:
        test(array, index + 1, index, count, min_count)


N = int(input())
array = [list(map(int, input().split())) for i in range(N)]
for line in array:
    line.append(line[0] - line[1])
    line.append(line[0] + line[1])
array = sorted(array, key=lambda x: x[3])

count = 0
max_r = -float('inf')
for i in range(N):
    current = array[i]
    # print(max_r)
    # print(current[2])
    if current[2] >= max_r:
        # print("残す")
        count += 1
        max_r = current[3]
# test(array, 0, -1, 0, min_count)
print(count)
