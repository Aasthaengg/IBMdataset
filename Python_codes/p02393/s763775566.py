x = map(int, raw_input().split())
for i in range(len(x)-1):
    for j in range(len(x)-i-1):
        if x[j] > x[j+1]:
            tmp = x[j+1]
            x[j+1] = x[j]
            x[j] = tmp
print x[0], x[1], x[2]