input_list = [int(input()) for i in range(5)]
k = int(input())
for i in range(1, 5):
    if abs(input_list[0] - input_list[i] ) > k:
        print(":(")
        exit()
for i in range(2, 5):
    if abs(input_list[1] - input_list[i]) > k:
        print(":(")
        exit()
for i in range(3, 5):
    if abs(input_list[2] - input_list[i]) > k:
        print(":(")
        exit()
for i in range(4, 5):
    if abs(input_list[3] - input_list[i]) > k:
        print(":(")
        exit()
print("Yay!")
