n = int(input())
arr = []
for i in range(n):
    arr.append(int(input())-1)
now = 0
c = 0
while True:
    if now == 1:
        print(c)
        break
    if c >= n:
        print(-1)
        break
    c += 1
    now = arr[now]