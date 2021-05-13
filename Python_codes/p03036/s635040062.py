r,d,x=map(int,input().split())
koke=[0]*11
koke[0]=x
for i in range(10):
    koke[i+1]=r*koke[i]-d
for i in range (10):
    print(koke[i+1])