a,b = map(int,input().split())
x = 1
cnt = 0
while x < b:
    x = x -1 + a
    cnt += 1

print(cnt)