n = int(input())
a = [int(input()) for i in range(n)]
sorted_list = sorted(a, reverse=True)
a_max = sorted_list[0]
a_sec = sorted_list[1]
for i in range(n) :
    if a[i] != a_max :
        print(a_max)
    else :
        print(a_sec)
