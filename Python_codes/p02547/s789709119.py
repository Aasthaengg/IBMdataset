N = int(input())
D = [tuple(map(int, input().split())) for _ in range(N)]
count = 0
for d1, d2 in D:
    if d1 == d2:
        count += 1
        if count >= 3:
            print('Yes')
            quit()
    else:
        count = 0

print('No')