
num = int(input())
max_value = float("-inf")
min_value = float("inf")

for i in [int(input()) for x in range(num)]:

    if max_value < (i - min_value):
        max_value = i - min_value

    if min_value > i:
        min_value = i

print(max_value)