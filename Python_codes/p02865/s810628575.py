# coding: utf-8
# Your code here!

n = int(input())

# print(n)

count = 0
div, mod = divmod(n, 2)
for i in range(1, n // 2 + 1):
    a = i
    b = n - a
    
    if a == b:
        continue

    # print("{}, {}".format(a, b))
    count += 1
    
print(count)