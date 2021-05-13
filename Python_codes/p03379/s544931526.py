n = int(input())
x = list(map(int,input().split()))
sort_x = sorted(x)
m1 = n // 2 - 1
m2 = n // 2
for i in range(n):
    if x[i] <= sort_x[m1]:
        print(sort_x[m2])
    elif x[i] >= sort_x[m2]:
        print(sort_x[m1])