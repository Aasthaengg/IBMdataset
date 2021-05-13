n = int(input())

a = [0] * n
for i in range(n):
    a[i] = int(input())

loop = [0] * n


if (2 not in a):
    print(-1)
    exit()

tar_index = 0
loop[0] = 1
# 何回目で２に到達するか
count = 0

while True:
    tar_index = a[tar_index] - 1
    #print(count, tar_index)
    count += 1

    if (tar_index == 1):
        print(count)
        exit()

    # 一回行った場所に戻ると、循環してるのでOUT
    if (loop[tar_index] == 1):
        print(-1)
        exit()

    loop[tar_index] = 1
