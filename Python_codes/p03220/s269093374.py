from decimal import Decimal
n = int(input())
t,a = map(int,input().split())
hl = list(map(int,input().split()))

num = 10**9
diff = 10**9
for i in range(n):
    tmp = t - Decimal(hl[i] * 0.006)
    tmp_diff = abs(tmp-a)
    
    if tmp_diff < diff:
        num = i + 1
        diff = tmp_diff
print(num)