n = int(input())
li = []
count = 0
for i in range(n):
    lr = list(map(int,input().split()))
    li.append(lr)
for j in range(n):
    count += li[j][1] - li[j][0] + 1
print(count)