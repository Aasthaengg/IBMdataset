n = int(input())
L = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

d = [0] * (n - 1)
if (L[0] > L[1]):
    d[0] = -1
elif (L[0] < L[1]):
    d[0] = 1

for i in range(n):
    if (i == 0):
        continue
    elif (i == n - 1):
        break
    else:
        if (L[i] < L[i + 1]):
            d[i] = 1
        elif (L[i] > L[i + 1]):
            d[i] = -1

prev = 0
count = 0
for i in range(len(d)):
    if (i == 0):
        prev = d[i]
        continue
    if (prev == 1):
        if (d[i] == 1):
            continue
        elif (d[i] == 0):
            continue
        else:
            count += 1
            prev = 0
    elif (prev == -1):
        if (d[i] == -1):
            continue
        elif (d[i] == 0):
            continue
        else:
            count += 1
            prev = 0
    elif (prev == 0):
        if (d[i] == 1):
            prev = 1
        elif (d[i] == -1):
            prev = -1

print(count + 1)
