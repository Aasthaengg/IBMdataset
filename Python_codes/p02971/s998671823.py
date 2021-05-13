n = int(input())
a = [int(input()) for _ in range(n)]

a_sorted = sorted(a)
a_max1 = a_sorted[-1]
a_max2 = a_sorted[-2]
for a_i in a:
    if a_i == a_max1:
        print(a_max2)
    else:
        print(a_max1)
