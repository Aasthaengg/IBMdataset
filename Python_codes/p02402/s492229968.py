n = int(input())
l = list(map(int,input().split()))

mi = l[0]
ma = l[0]
s = 0
for i in l :
    if i > ma :
        ma = i
    if i < mi :
        mi = i
    s += i
print(mi,ma,s)