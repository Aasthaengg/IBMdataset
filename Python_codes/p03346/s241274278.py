n = int(input())
p = [int(input()) for i in range(n)]
index = [None]*(n+1)
for i in range(n):
    index[p[i]] = i
length = 0
now = 0
max_length = 0
for i in range(1, n+1):
    if index[i] >= now:
        now = index[i]
        length += 1
    else:
        now = index[i]
        max_length = max(max_length, length)
        length = 1
max_length = max(max_length, length)

print(n-max_length)
