n = int(input())
num_list = list(map(int, input().split()))

tmp_list = []
cnt = 0
for i in range(0, n-2, 1):
    tmp = num_list[i:i+3]
    if tmp[0] < tmp[1] and tmp[1] < tmp[2]:
        cnt += 1
    elif tmp[2] < tmp[1] and tmp[1] < tmp[0]:
        cnt += 1

print(cnt)