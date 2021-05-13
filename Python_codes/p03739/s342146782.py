import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt1, now = 0, 0

for i in range(n):
    now += a[i]
    
    if i%2==0:
        if now<=0:
            cnt1 += 1-now
            now = 1
    else:
        if now>=0:
            cnt1 += now+1
            now = -1
    
cnt2, now = 0, 0

for i in range(n):
    now += a[i]
    
    if i%2==1:
        if now<=0:
            cnt2 += 1-now
            now = 1
    else:
        if now>=0:
            cnt2 += now+1
            now = -1

print(min(cnt1, cnt2))