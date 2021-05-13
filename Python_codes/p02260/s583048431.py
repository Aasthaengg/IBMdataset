# -*- coding:utf-8 -*-

def selection_sort(num_list):
    num_swap = 0
    for i in range(len(num_list)):
        mini = i
        for j in range(i, len(num_list)):
            if num_list[j] < num_list[mini]:
                mini = j
        if i != mini:
            num_list[i], num_list[mini] = num_list[mini], num_list[i]
            num_swap = num_swap + 1
    return num_swap, num_list

def show_list(list):
    i = 0;
    while(i < len(list)-1):
        print(list[i], end=" ")
        i = i + 1
    print(list[i])

num = int(input())
num_list = [int(x) for i, x in enumerate(input().split()) if i < num]
num_swap, num_list = selection_sort(num_list)
show_list(num_list)
print(num_swap)