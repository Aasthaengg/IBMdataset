r,d,x = map(int,input().split())
l = [0]*15
l[0] = x
for i in range(1,15):
    l[i] = r * l[i-1] - d
for i in range(1,11):
    print(l[i])