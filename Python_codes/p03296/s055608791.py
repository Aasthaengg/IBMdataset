# coding: utf-8

n = int(input().rstrip())

numbers = list(map(int, input().rstrip().split(" ")))

start = 0
ans = 0
for i in range(1,n):
    if numbers[i] != numbers[i - 1]:
        tmp = i - start
        ans += int(tmp/2)
        start = i

ans += int((n-start)/2)

print(ans)
