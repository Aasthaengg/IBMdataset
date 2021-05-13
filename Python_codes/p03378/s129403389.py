n, m, x = map(int,input().split())
a = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
for i in range(x):
    if i in a:
        cnt1 += 1
for j in range(x,n+1):
    if j in a:
        cnt2 += 1
        
print(min(cnt1, cnt2))