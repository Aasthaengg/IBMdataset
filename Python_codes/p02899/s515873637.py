N = int(input())

ans = [0]*N
count = 1
for i in input().split():
    i = int(i)
    ans[i-1] = count
    count += 1

for i in ans:
    print(i, end=" ")
