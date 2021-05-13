import heapq
X, Y, A, B, C = map(int, input().split())
P = sorted([int(i) for i in input().split()], reverse=True)
Q = sorted([int(i) for i in input().split()], reverse=True)
R = sorted([int(i) for i in input().split()], reverse=True)


hq = P[:X]+Q[:Y]
ans = sum(hq)
heapq.heapify(hq)  # リストhqのheap化

i = 0
while hq and i < len(R):
    t = heapq.heappop(hq)  # heap化されたリストhqから最小値を削除＆その最小値を出力
    if R[i] > t:
        ans = ans - t + R[i]
        i += 1
    else:
        break
print(ans)
