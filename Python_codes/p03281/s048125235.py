N = int(input())

total = 0
for i in range(N-1):
    cnt = 0
    for j in range(N-i):
        if (N-i) % (N-i-j) == 0:
            cnt += 1 
    if cnt == 8 and (N-i) % 2 != 0:
        total += 1
print(total)