from collections import Counter
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
A = iil()
c = Counter(A)

ans = 0

for k,v in c.items():
    if v < k:
        ans += v
    else:
        ans += v-k
print(ans)