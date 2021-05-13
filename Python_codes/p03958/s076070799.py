k, t = map(int, input().split())
a_list = [[int(value), index] for index, value in enumerate(input().split())]
ans = 0
prev = -1
for i in range(k):
    a_list.sort(reverse=True)
    index = 0
    if prev == a_list[index][1]:
        if len(a_list) > 1:
            index += 1
        else:
            ans += 1
    prev = a_list[index][1]
    if a_list[index][0] == 1:
        a_list.pop(index)
    else:
        a_list[index][0] -= 1
print(ans)