from collections import*
i = eval("Counter(list(map(int, input().split()))),"*4)
print("YNEOS"[any(i[1][j] < k for j, k in i[3].items())::2])