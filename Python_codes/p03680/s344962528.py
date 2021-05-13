N = int(input())
l = [int(input()) for i in range(N)]
index = 0
count = 0
for j in range(N):
    index = l[index] - 1
    count += 1
    if index == 1:
        print(count)
        exit()
print(-1)