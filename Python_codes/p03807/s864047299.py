n = int(input())
a = list(map(int,input().split()))

cnt_odd = 0
for i in range(n):
    if a[i]%2==1:
        cnt_odd += 1

if cnt_odd % 2 ==1:
    print("NO")
else:
    print("YES")