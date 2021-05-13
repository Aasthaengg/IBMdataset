N = int(input())

a = list(map(int,input().split()))

avg = sum(a)/N

near_num = 101
res = 0

for i in range(N):
    if abs(a[i]-avg) < near_num:
        res = i
        near_num = abs(a[i]-avg)
print(res)