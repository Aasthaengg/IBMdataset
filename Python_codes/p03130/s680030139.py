def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
l = []
for i in range(3):
    a,b = iim()
    l.append(a)
    l.append(b)

for i in range(1,5):
    if l.count(i) == 3:
        print('NO')
        exit()
print('YES')

