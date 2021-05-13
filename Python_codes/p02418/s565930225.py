text_list = []

for x in range(2):
    if x != 1:
        text_list.append(input()*2)
    else:
        text_list.append(input())

print('Yes' if text_list[1] in text_list[0] else 'No')

