S_list = [int(input()) for i in range(3)]
n = (S_list[0]-S_list[1]) // S_list[2]

zankin = S_list[0]-(S_list[1] + n * S_list[2])
print(zankin)