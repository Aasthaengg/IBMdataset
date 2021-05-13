n = int(input())
l = list(map(int,input().split()))

mean = sum(l)/n
x=10**9+7
y=-1
for i in l:
    if x > abs(i-mean):
        x = abs(i-mean)
        y = i

print(l.index(y))