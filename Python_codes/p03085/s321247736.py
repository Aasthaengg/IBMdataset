b = input()
lst = [["A", "T"], ["G", "C"]]
print(lst[0][lst[0].index(b) - 1]) if b in lst[0] else print(lst[1][lst[1].index(b) - 1])