N = int(input())

lucas_list = [2, 1]
for i in range(2, 86+1):
    lucas_list.append(lucas_list[i-1] + lucas_list[i-2])
    
print(lucas_list[N])