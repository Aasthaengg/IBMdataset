num_house = int(input())
a = map(int, input().split())
house_list = list(a)

print(max(house_list) - min(house_list))
