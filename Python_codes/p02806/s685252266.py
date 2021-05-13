n = int(input())
li = [input().split() for _ in range(n)]
x = input()
flag = 0
ans = 0

for i in range(n):
    s = li[i][0]
    if flag == 1:
        ans += int(li[i][1])
    if x == s:
        flag = 1

print(ans)