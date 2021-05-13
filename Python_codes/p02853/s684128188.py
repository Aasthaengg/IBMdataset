X, Y = map(int, input().split())
tmp=0
if X==1 and Y==1:
    tmp+=400000

for i in (X, Y):
    if i==1:
        tmp+=300000
    elif i==2:
        tmp+=200000
    elif i==3:
        tmp+=100000
print(tmp)
