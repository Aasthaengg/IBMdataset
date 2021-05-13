def count_unit(ss,pp):
    count = 0
    for i in lst:
        if ss == i.lower():
            count = count + 1
    return count

s = str(input())
sum = 0
while True:
    lst = list(map(str, input().split()))
    if lst[0] == "END_OF_TEXT":
        print(sum)
        break
    else:
        sum += count_unit(s,lst)

