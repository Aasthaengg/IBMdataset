n = map( int, input())
a = list(map( int, input().split() ))
A_point = 0
B_point = 0
flag = 1

a.sort(reverse=True)

for point in a:
    if flag%2 == 1:
        A_point += point
        flag += 1
    elif flag%2 == 0:
        B_point += point
        flag += 1

print("{}".format(A_point-B_point))