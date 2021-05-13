N = int(input())
b = list(map(int, input().split()))
ans = []
for i in range(N):
    # それぞれの数字の余裕度を計算し、余裕度0で一番後ろのやつをとる
    d = -1
    for j in range(N-i):
        if (j+1)-b[j] == 0:
            d = j
    if d == -1:
        print(-1)
        exit()
    else:
        ans.append(b[d])
        del b[d]
[print(a) for a in ans[::-1]]