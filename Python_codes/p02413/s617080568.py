#!/usr/bin/python

r, c = map(int, input().strip().split(" "))

row_lists = list()
for _ in range(r):
    row_list = list(map(int, input().strip().split(" ")))
    row_list.append(sum(row_list))
    row_lists.append(row_list)

lastrow = [sum(i) for i in zip(*row_lists)]

row_lists.append(lastrow)

for r in row_lists:
    print(" ".join(map(str, r)))