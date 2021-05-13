a,b = map(int,input().split())
tmp = 0
for i in range(10001):
    if int(i * 0.08) == a and int(i * 0.10) == b:
        tmp = 1
        break
if tmp == 1:
    print(i)
else:
    print(-1)