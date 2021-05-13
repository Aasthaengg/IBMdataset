n = int(input())
a = list(map(int,input().split()))

lst = [0] * 8
s = 0

for i in a:
    if i >= 3200:
        s += 1
    else:
        i //= 400
        lst[i] += 1

colour = 0
for i in lst:
    if i >= 1:
        colour += 1

m = max(1, colour)
M = colour + s

print(m, M)
