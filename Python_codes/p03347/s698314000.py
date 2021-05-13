n = int(input())

p = [int(input()) for _ in range(n)]



count = 0
climing = 0

if p[0] !=0:
    print(-1)
    exit()

for index in range(len(p) - 1):
    current_num = p[index]
    next_num = p[index + 1]

    if current_num == next_num:
        count += current_num
    elif current_num + 1 == next_num:
        pass
    elif current_num > next_num:
        count += current_num
    else:
        # abort
        print(-1)
        exit()

# 終端処理
count += p[-1]
print(count)
