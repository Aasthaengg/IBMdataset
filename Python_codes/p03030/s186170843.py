n = int(input())
shop_list = []
for i in range(n):
    temp_list = list(input().split())
    temp_list[1] = int(temp_list[1])
    temp_list.append(i+1)
    shop_list.append(temp_list)

shop_list_sorted = sorted(shop_list,key=lambda x:(x[0],-x[1]))
for k in range(n):
    print(shop_list_sorted[k][2])
