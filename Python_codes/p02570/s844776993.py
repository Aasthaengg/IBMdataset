input_data = list(map(int, input().strip().split()))
if (input_data[0] / input_data[2] <= input_data[1]):
    print("Yes")
else:
    print("No")