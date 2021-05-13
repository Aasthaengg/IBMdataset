import math
n = int(input())
t = []
for i in range(n):
    t.append(int(input()))
if n == 1:
    print(t[0])
else:
    tmp = t[0]
    for i in range(1,n):
        div = math.gcd(tmp,t[i])
        tmp = (t[i] * tmp)//div
    print(tmp)
