import copy

N = int(input())

x = list(map(int,input().split()))
sort_x = copy.copy(x)
sort_x.sort()

center_num = (N-1) // 2

for l in x:
    if l <= sort_x[center_num]:
        print(sort_x[center_num+1])
    else:
        print(sort_x[center_num])
