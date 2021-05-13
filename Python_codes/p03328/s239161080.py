height=[]
for i in range(1,1000):
    height.append((1+i)*i//2)

a,b=map(int,input().split())
for i in range(998):
    if height[i+1]-height[i]==b-a:
        print(height[i]-a)