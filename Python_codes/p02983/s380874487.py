l, r=map(int,input().split())
if r-l>=2019:
    minimum=0
else:
    left,right=l%2019,r%2019
    minimum=2018**2
    for i in range(left,right+1):
        for j in range(i+1,right+1):
            minimum=min(minimum,i*j%2019)
print(minimum)