N = int(input())
x_list = list(map(int, input().split()))
sorted_x = sorted(x_list)

medi = N//2
l = sorted_x[medi-1]
r = sorted_x[medi]
for x in x_list:
    if x < r:
        print(r)
    else:
        print(l)
