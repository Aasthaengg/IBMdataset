x=100000
for i in range(int(input())):
    x*=1.05
    if x%1000!=0:
        x+=1000-x%1000
print(int(x))
