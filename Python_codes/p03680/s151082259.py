N = int(input())

a = [int(input()) for i in range(N)]
index=0

for i in range(N):
    next = a[index]
    if next==2:
        count = i+1
        break
    index = next-1
    count = -1

print(count)