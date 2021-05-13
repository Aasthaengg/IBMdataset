import sys
N = int(input())
lst = [int(input())-1 for _ in range(N)]

next = 0
count = 0
for i in range(len(lst)):
    next = lst[next]
    count+=1
    if next == 1:
        print(count)
        sys.exit()
print(-1)

