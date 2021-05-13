a,b=map(int,input().split())
mozi = ''
if a > b:
    for i in range(0,a):
        mozi = mozi + str(b)
else:
    for i in range(0,b):
        mozi = mozi + str(a)
print(mozi)