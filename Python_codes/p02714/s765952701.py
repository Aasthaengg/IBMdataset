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

n = int(input())
s = input()

r = [i+1 for i, x in enumerate(s) if x == 'R']
g = [i+1 for i, x in enumerate(s) if x == 'G']
b = [i+1 for i, x in enumerate(s) if x == 'B']

c = 0
for i in r:
    for j in g:
        if binary_search(b, 2*i - j) != -1:
            c += 1
        if binary_search(b, 2*j - i) != -1:
            c += 1
        if binary_search(b, (i+j)/2) != -1:
            c += 1

ans = (len(r)*len(g)*len(b) - c)
print(ans)