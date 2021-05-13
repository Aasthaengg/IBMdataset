def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
k = ii()

now = 1
for i in range(n):
    if now < k:
        now *= 2
    else:
        now += k
print(now)