import statistics
n = int(input())
a_li = list(map(int,input().split()))
median_low = statistics.median_low(a_li)
median_high = statistics.median_high(a_li)
for i in range(n):
    if a_li[i] <= median_low:
        print(median_high)
    else:
        print(median_low)