a,b,n = map(int, input().split())

def ma(k):
    s = a * k / b
    t = k / b
    ss = s // 1
    tt = (t // 1) * a
    return ss - tt

if(n < b):
    print(str(int(ma(n))))
else:
    print(str(int(ma(b-1))))