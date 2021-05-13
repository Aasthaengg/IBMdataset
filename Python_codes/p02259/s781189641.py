#
# coding: utf-8
 
def bubbleSort(arr, n):
 
    flag = True
    swap_num = 0
 
    while flag:
        flag = False
        for j in xrange(n-1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swap_num += 1
                flag = True
        pass
    return swap_num
 
 
n = int(raw_input())
arr = map(int, raw_input().split())
 
num = bubbleSort(arr, n)
print " ".join(map(str, arr))
print num