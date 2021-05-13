N, H, W = list(map(int, input().split()))
length_datas = [input() for i in range(N)]
count = 0
for data in length_datas:
    A, B = list(map(float, data.split()))
    if (A >= H) and (B >= W):
        count += 1

print(count)
