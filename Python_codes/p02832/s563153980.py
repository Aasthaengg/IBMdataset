N = int(input())
A = [int(s) for s in input().split(' ')]
head = 1
count = 0
for a in A:
    if a == head:
        head += 1
        continue
    else:
        count += 1
if head == 1:
    print(-1)
else:
    print(count)

