N = int(input())
a_list = list(map(int, input().split()))
max_num = max(a_list)
min_num = min(a_list)
result = []
if abs(max_num) >= abs(min_num):
    max_index = a_list.index(max_num)
    for i, a in enumerate(a_list):
        if a < 0:
            a_list[i] += max_num
            result.append((max_index + 1, i + 1))

    for i in range(N - 1):
        if a_list[i] > a_list[i + 1]:
            result.append((i + 1, i + 2))
            a_list[i + 1] += a_list[i]
    print(len(result))
    for v1, v2 in result:
        print(v1, v2)

else:
    min_index = a_list.index(min_num)
    for i, a in enumerate(a_list):
        if a > 0:
            a_list[i] += min_num
            result.append((min_index + 1, i + 1))

    for i in reversed(range(N - 1)):
        if a_list[i] > a_list[i + 1]:
            result.append((i + 2, i + 1))
            a_list[i] += a_list[i + 1]
    print(len(result))
    for v1, v2 in result:
        print(v1, v2)
    exit()
