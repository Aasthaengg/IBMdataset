n = int(input())
a = list(map(int,input().split()))
list = [0]*8
cnt =0
for i in range(n):
    if a[i]//400 >= 8:
        cnt += 1
    else:
        list[a[i]//400] += 1
if cnt == n:
    print(1,min(cnt,8))
else:
    print(8-list.count(0),8-list.count(0)+cnt)