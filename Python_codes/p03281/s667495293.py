n = int(input())
cnts = 0

for i in range(1,n+1):
    cnt = 0

    for j in range(1,n + 1):
        if i % j == 0:
            cnt += 1
    if (cnt == 8)&(i%2 != 0):
        cnts += 1

print(cnts)