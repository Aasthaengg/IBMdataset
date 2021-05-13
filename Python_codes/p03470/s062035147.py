N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

d.sort()

count = 0
last = 0
for i in range(0,N):
    if last < d[i] :
        count += 1
        last = d[i]

print(count)