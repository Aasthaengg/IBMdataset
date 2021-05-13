def grand_garden(n, h):

    count = 0
    j = 100
    for i in range(n):
        if h[i] != 0:
            j = i
            break
    if j == 100:
        return count

    while h[j] != 0:
        l = j  # 左はしきめる
        r = l  # 動く右はし
        for k in range(l, n):  # 右端はZeroでないかぎりのばす、ゼロになる最初の位置を取得、すべてゼロでなければ配列の右端
            if k == n-1 and h[k] != 0:
                r = n
            elif h[k] == 0:
                r = k
                break

        min_val = min(h[l:r])  # 右はしから左はしまでの最小値を取得
        for x in range(l, r):  # 各要素から共通の最小値を差し引く
            h[x] -= min_val
        count += min_val  # 最小値分カウントを追加
        if h[j] == 0:  # もしも左端がゼロだったらゼロでない最初の位置へ移動
            for t in range(j, n):
                if h[t] != 0:
                    j = t
                    break

        if j >= n:
            break
    return count


def main():
    n = int(input())
    h = list(map(int, input().split()))

    answer = grand_garden(n, h)
    print(answer)


'''
数列に0が含まれない最大の幅を取得(0ではない最小の左から最大の右でもよいのか)
その幅に含まれる要素高さを1ずつへらす、
count +=1

0 <= l,r <= n-1
while True:
    if h[i] == 0:
        l += 1
        i += 1
        continue
        if l >= n:
            break

   for i in range(n):
        if h[i] != 0:
            l = i
            r = l
            for j in range(l, n):
                if h[j] != 0:
                    r += 1
            for k in range(l, r):
                h[k] -= min(h[l:r])
#            if h[l] != 0:
#                i -= 1
            count += 1


'''


if __name__ == "__main__":
    main()
