n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0

for i in a:
    if i > x:
        cnt1 += 1
    else:
        cnt2 += 1
        
print(min(cnt1, cnt2))