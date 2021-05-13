from sys import stdin
k = int(stdin.readline().rstrip())
num = 7
flag = 0
for i in range(1, k + 1):
    if num % k == 0:
        flag = 1
        break
    num = (num * 10 + 7) % k
if flag == 1:
    print(i)
else:
    print(-1)