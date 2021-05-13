H, W, M = map(int, input().split())
hw = set()
sum_h = [0] * W
sum_w = [0] * H
for _ in range(M):
    h, w = map(int, input().split())
    hw.add((h, w))
    h -= 1
    w -= 1
    sum_h[w] += 1
    sum_w[h] += 1


max_h = max(sum_h)
max_w = max(sum_w)

new_H = [h for h in range(H) if sum_w[h] == max_w]
new_W = [w for w in range(W) if sum_h[w] == max_h]

max_num = max_h + max_w - 1
for i in new_H:
    for j in new_W:
        if (i + 1, j + 1) not in hw:
            print(max_h + max_w)
            exit()
        else:
            continue
        break

print(max_num)
