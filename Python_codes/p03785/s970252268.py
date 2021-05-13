def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,c,k = iim()
time = []
for _ in range(n):
    time.append(ii())

time.sort()

bus = 0
fst = time[0]
ans = 0
for item in time:
    if bus <= c-1 and item <= k+fst:
        bus += 1
    else:
        bus = 1
        ans += 1
        fst = item

print(ans if bus == 0 else ans+1)