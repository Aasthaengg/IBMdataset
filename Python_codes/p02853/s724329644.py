l = [300000,200000,100000]
a,b = map(int,input().split())
res = 0 
if a in range(1,4):
    res +=l[a-1]
if b in range(1,4):
    res +=l[b-1]
if a == b and a==1:
    res+=400000
print(res)