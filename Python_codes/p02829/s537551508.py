lst = [1, 2, 3]
for _ in [0] * 2:
    lst.remove(int(input()))
print(lst[0])