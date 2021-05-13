#58
import decimal
n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

near = float("inf")
num = 0

for i in h:
    x = t - i*decimal.Decimal("0.006")
    if near > abs(a-x):
        near = abs(a-x)
        num = i
        
print(h.index(num)+1)