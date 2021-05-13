a_lst = list(map(abs, map(int, input().split(" "))))

a_lst.sort()

total = 0
previous = a_lst[0]
for i in a_lst[1:]:
    total += (i - previous)
    previous = i

print(total)
