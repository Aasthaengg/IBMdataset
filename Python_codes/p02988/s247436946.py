n = int(input())
p = list(map(int, input().split()))
num = 0
for i in range(0,n-2,1):
    i2 = i+1
    i3 = i+2
    if p[i]<p[i2]<p[i3] or p[i]>p[i2]>p[i3]:
        num += 1
print(num)