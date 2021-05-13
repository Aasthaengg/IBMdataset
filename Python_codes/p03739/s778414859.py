from sys import stdin
import sys
import math

n = int(input())
a = list(map(int, stdin.readline().rstrip().split()))

#print(odd)
#print(pair)


## pair > odd
count_pair = 0
current_sum = 0
diff = 0
for i in range(len(a)):
    if i % 2 == 0:
        if current_sum + a[i] < 1:
            diff = 1 - (current_sum + a[i])
            count_pair += diff
        else:
            diff = 0
    elif i % 2 == 1:
        if current_sum + a[i] > -1:
            diff = -1 - (current_sum + a[i])
            count_pair += -1 * diff
        else:
            diff = 0

    current_sum += a[i] + diff
    if current_sum == 0:
        print("Error")

# odd > pair
count_odd = 0
current_sum = 0
diff = 0
i=0
for i in range(len(a)):
    if i % 2 == 1:
        if current_sum + a[i] < 1:
            diff = 1 - (current_sum + a[i])
            count_odd += diff
        else:
            diff = 0
    elif i % 2 == 0:
        if current_sum + a[i] > -1:
            diff = -1 - (current_sum + a[i])
            count_odd += -1 * diff
        else:
            diff = 0


    current_sum += a[i] + diff
    if current_sum == 0:
        print("Error")


print(min(count_odd, count_pair))
