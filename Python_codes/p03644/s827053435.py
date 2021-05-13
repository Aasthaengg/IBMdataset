n = int(input())
ans = 1
elem_list = []

for i in range(7):
    elem_list.append(2**i)

for i in elem_list[::-1]:
    if i <= n:
        print(i)
        break