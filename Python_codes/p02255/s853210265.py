import sys

n = input()
sort_list = list()

sort_list = map(int, raw_input().split())

for i in range(0,n):
    
    
    tmp = sort_list[i]
    j = i - 1
    while j >= 0 and sort_list[j] > tmp:
        sort_list[j+1] = sort_list[j]
        j = j - 1

    sort_list[j+1] = tmp


    for k in range(0,n):
        sys.stdout.write(str(sort_list[k]))
        if k is not n - 1:
            sys.stdout.write(" ")
        elif i is not n - 1:
            sys.stdout.write("\n")
            
print("")

