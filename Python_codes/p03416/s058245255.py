a, b = map(int, input().split())
number_list = list(range(a, b + 1))
ans = []
for i in range(len(number_list)):
    str_number = str(number_list[i])
    len_number = len(str_number)
    count = 0
    for j in range(len_number // 2):
        if str_number[j] != str_number[-1 - j]:
            break
        count += 1
    if count == len_number // 2:
        ans.append(str_number)
print(len(ans))
