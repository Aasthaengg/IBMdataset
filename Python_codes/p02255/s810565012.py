# -*- coding : utf-8 -*-

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        show_list(list)
        while(j >= 0 and list[j] > key):
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = key
    show_list(list)
    return list

def show_list(list):
    i = 0;
    while(i < len(list)-1):
        print(list[i], end=" ")
        i = i + 1
    print(list[i])

list_length = int(input())
list = [int(x) for x in input().split(" ")]
insertion_sort(list)