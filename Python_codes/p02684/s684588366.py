import heapq

def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1            # 見つからなかった場合

n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))
way = [0]
hq = [0]
heapq.heapify(hq)
posi = 0
cycle = 0
while True:
    if binary_search(hq, a[posi]) != -1:
        rest = way.index(a[posi])
        cycle -= (rest - 1)
        break
    way.append(a[posi])
    heapq.heappush(hq, a[posi])
    posi = a[posi]
    cycle += 1
# print(way)
# print(cycle)
if k < len(way):
    print(way[k] + 1)
else:
    print(way[(k-rest) % cycle + rest] + 1)