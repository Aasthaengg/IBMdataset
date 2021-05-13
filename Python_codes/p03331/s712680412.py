def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
ans = 100
def colsum(s):
    ret = 0
    for i in s:
        ret += int(i)
    return ret

for i in range(1,n):
    cand = colsum(str(i))+colsum(str(n-i))
    ans = min(cand,ans)
print(ans)