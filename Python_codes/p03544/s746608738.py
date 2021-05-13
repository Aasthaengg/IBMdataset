n = int(input())
l_list = [2, 1]
if n < 2 :
    print(l_list[n])
else :
    for i in range(2,n+1) :
        new = l_list[i-1] + l_list[i-2]
        l_list.append(new)
    print(l_list[n])
