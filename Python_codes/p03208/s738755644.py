#普通にソートしてから、配列のK個づつ区切ってパターンを調べればN - K + 1回の比較で行ける

N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort()

distances = [h[i + K -1] - h[i] for i in range(N -K + 1)]
ans = min(distances)
print(ans)