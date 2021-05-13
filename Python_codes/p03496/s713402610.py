n = int(input())
a = [int(i) for i in input().split()]
a_max = max(a)
a_min = min(a)

abs_max = a_min if abs(a_min) > abs(a_max) else a_max
abs_max_index = a.index(abs_max)


print(2*n-1)

total = 0

for i in range(n):

    print(abs_max_index+1, i+1)
    a[i] += abs_max

my_range, next_index_diff = (
    list(range(n-1)), 1) if abs_max > 0 else (list(range(n-1, 0, -1)), -1)


while my_range:

    index = my_range.pop(0)

    print(index+1, index+1+next_index_diff)
    a[index+next_index_diff] += a[index]
