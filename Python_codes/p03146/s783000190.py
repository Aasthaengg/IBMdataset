s = int(input())

answer_list = []
answer_list.append(s)
count = 1
while True:
    count += 1
    next_s = 0
    if s % 2 == 0:
        next_s = s // 2
    else:
        next_s = s * 3 + 1
    s = next_s
    if s in answer_list:
        print(count)
        exit()
    answer_list.append(s)
