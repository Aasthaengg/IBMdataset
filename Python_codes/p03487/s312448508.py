from collections import Counter

N = int(input())
a = list(map(int, input().split()))

num_removal = 0
for digit, count in Counter(a).items():
    if digit > count:
        num_removal += count
    else:
        num_removal += (count - digit)
print(num_removal)
