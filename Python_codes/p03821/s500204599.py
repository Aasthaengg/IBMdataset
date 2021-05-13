def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = []
for _ in range(n):
    l.append(iil())

ans = 0
for item in l[::-1]:
    a = item[0]+ans
    if a%item[1] != 0:
        ans += item[1]-a%item[1]

print(ans)