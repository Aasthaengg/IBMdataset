s1 = input()
s2 = input()
list_s1 = list(s1)
list_s2 = list(s2)
len_s1 = len(s1)
len_s2 = len(s2)
change_count_min = len_s2
for i in range(len_s1 - len_s2 + 1):
    change_count = len_s2
    for j in range(len_s2):
        if list_s1[j+i] == list_s2[j]:
            change_count -= 1
    if change_count < change_count_min:
        change_count_min = change_count
print(change_count_min)