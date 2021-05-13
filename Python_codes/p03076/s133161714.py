cook_list = []
cook_list_2 = []

for i in range(5):
    cook_list.append(int(input()))

for c in cook_list:
    cook_list_2.append(((c+9)//10)*10)
    
max_diff = 0
for j in range(5):
    if cook_list_2[j] - cook_list[j] >= max_diff:
        max_diff = cook_list_2[j] - cook_list[j]
    
ans = sum(cook_list_2) - max_diff
print(ans)