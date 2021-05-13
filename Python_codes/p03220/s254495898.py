N = int(input())
T, A = map(int, input().split())
height_list = list(map(int, input().split()))

temperature_diff_list = []
for height in height_list:
  temperature = T - height*0.006
  temperature_diff = temperature - A if temperature > A else A - temperature 
  temperature_diff_list.append(temperature_diff)

print(temperature_diff_list.index(min(temperature_diff_list)) + 1)