import sys
n = int(input())
a = [int(i) for i in input().split()]
if not 1 in a:
    print(-1)
    sys.exit()
target = 1
count = 0
for i in a:
    if i == target:
        target += 1
    else:
        count += 1
print(count)