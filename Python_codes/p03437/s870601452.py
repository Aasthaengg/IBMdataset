X,Y = map(int,input().split())
flag = -1
if X!=Y:
    for i in range(1,10**9//(X)+1):
        if i*X%Y!=0:
            flag = i*X
            break
print(flag)