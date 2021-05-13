r,D,x = map(int,input().split())
tmp = x
for i in range(1,11):
    tmp = r*tmp - D
    x += D
    print(tmp)
