s = input()
n = int(s)

blues = []
reds = []

count = []
for i in range(n):
    count.append(0)
max_count = 0

for i in range(n):
    p = input()
    blues.append(p)

v = input()
m = int(v)

for i in range(m):
    q = input()
    reds.append(q)

for i in range(len(blues)):
    for j in range(len(blues)):
        if blues[i] == blues[j]:
            count[i] += 1

for i in range(len(blues)):
    for j in range(len(reds)):
        if blues[i] == reds[j]:
            count[i] -= 1

for i in range(len(count)):
    max_count = max(max_count, count[i])

print(max_count)
        
