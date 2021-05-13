# coding: utf-8
# Your code here!

k, x = map(int, input().split())

# print(k)
# print(x)


l = [str(i) for i in range((x - k + 1), x + k)]

print(' '.join(l))