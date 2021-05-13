def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b,c = iim()
num = a%b

for i in range(1,b):
    if (num*i)%b == c:
        print('YES')
        exit()
print('NO')