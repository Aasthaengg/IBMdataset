from math import sqrt
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
# p=1
d = [0.0 for i in range(3)]
var = 0
for i in range(n):
    temp = abs(x[i]-y[i])
    if var < temp:
        var = temp
    for j in range(3):
        d[j]+=temp**(j+1)

for i in range(3):
    print(d[i]**(1/(i+1)))
print(float(var))
