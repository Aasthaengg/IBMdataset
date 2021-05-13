n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(x)
med_minus = x_sort[n//2-1]
med_plus = x_sort[n//2]
for i in range(n):
    if x[i] <= med_minus:
        print(med_plus)
    elif x[i] >= med_plus:
        print(med_minus)
