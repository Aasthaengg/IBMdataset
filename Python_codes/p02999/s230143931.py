# coding: utf-8
# Your code here!
data = input()
data_list = data.split(" ")
data_list[0] = int(data_list[0])
data_list[1] = int(data_list[1])

if data_list[0] < data_list[1]:
    print(0)
else:
    print(10)
    
