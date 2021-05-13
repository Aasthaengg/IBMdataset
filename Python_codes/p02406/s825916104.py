a = int(input())
x=0
y=[]
while x<a:
    x+=1
    if "3" in str(x) or x%3==0:
        y.append(str(x))
print(" "+" ".join(y))