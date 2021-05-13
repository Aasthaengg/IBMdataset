import sys

n, k = map(int, input().split())

l = list(map(int, input().split()))

# l.sort()

# max_length = 0
# for item in l[n-1:n-k-1:-1]:
#     max_length += item

# print("{}".format(max_length))

l.sort(reverse=True)

max_length = 0
for i in range(k):
    max_length += l[i]

print("{}".format(max_length))