n,h,w = [int(i) for i in input().split()]
_ = 0
for i in range(n):
    __ = [int(j) for j in input().split()]
    if __[0]>=h and __[1]>=w:
        _+=1
print(_)