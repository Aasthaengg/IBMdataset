x,y=map(int,input().split())
a=[x]
while a[-1]<=y:
    a.append(a[-1]*2)
print(len(a)-1)