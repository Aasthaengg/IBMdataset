n = int(input())
x_1 = list(map(int, input().split()))
x_2 = sorted(x_1)
median_1 = x_2[n//2-1]
median_2 = x_2[n//2]
for v in x_1:
    if v <= median_1:
        print(median_2)
    else:
        print(median_1)