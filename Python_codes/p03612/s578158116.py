def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
P = iil()
ans = 0
flag = False
for i in range(n-1):
    if flag:
        flag = False
        continue
    if P[i] == i+1:
        ans += 1
        flag = True
if P[-1] == n and flag == False:
    ans += 1
print(ans)
