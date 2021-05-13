def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
l = iil()
count = 0
for i in l:
    if i%2 == 1:
        count += 1
if count%2 == 0:
    print('YES')
else:
    print('NO')