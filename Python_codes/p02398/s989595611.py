n = list(map(int, input().split()))
l = list(range(n[0], n[1]+1))
i = n[2]
j = 0
for a in l:
    if (i % a == 0):
        j += 1
print(j)