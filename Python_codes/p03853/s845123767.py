H, W = [int(i) for i in input().split()]
cc = []
for _ in range(H):
    cc.append(input())

for i in range(2 * H):
    print(cc[i // 2])
