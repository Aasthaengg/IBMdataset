N = int(input())
l = list(map(int, input().split()))

exist_dict = {}
first_max = 0
second_max = 0

for i in l:
    if i in exist_dict:
        if exist_dict[i]==1 and i > first_max:
            second_max = first_max
            first_max = i
        elif exist_dict[i]==3 and i==first_max:
            second_max = i
        elif exist_dict[i]==1 and i > second_max:
            second_max = i
    
        exist_dict[i] = exist_dict[i] + 1
    else:
        exist_dict[i] = 1
    # print("first_max"+str(first_max))
    # print("second_max"+str(second_max))
    # print("exist_dict"+str(exist_dict))    
print(first_max*second_max)
