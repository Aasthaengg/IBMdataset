n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if sum(a) < sum(b):
    print(-1)
    exit(0)
ans = 0
tarinai = 0
yobun = []
for i in range(n):
    if a[i] < b[i]:
        ans += 1    
        tarinai += b[i] - a[i]
    elif a[i] > b[i]:
        yobun.append(a[i] - b[i])
if ans == 0:
    print(0)
    exit(0)
yobun.sort(reverse=True) 
m = len(yobun)
total = 0
for i in range(m):  
    total += yobun[i]
    if total >= tarinai:
        ans += i + 1
        break
print(ans)
