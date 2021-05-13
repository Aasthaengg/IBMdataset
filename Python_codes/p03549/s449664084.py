n,m = map(int,input().split())
a = m*1900+(n-m)*100
b = 0.5**m
ans = 0
count = 1
for i in range(1,100000):
    ans += i*count*b
    count -= b*count
print(round(a*ans))