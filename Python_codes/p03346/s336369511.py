n = int(input())
p = [int(input()) for _ in range(n)]

lst = [0] * (n + 1)
for num in p:
    bfo = lst[num - 1]
    if bfo == 0:
        lst[num] = -1
    elif bfo < 0:
        lst[num] = num - 1
        lst[num - 1] -= 1
    elif bfo > 0:
        lst[num] = bfo
        lst[bfo] -= 1
print(n + min(lst))
