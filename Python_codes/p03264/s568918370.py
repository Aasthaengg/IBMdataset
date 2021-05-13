k = int(input())
count_odd = 0
count_even = 0
for i in range(1, k+1):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_odd*count_even)