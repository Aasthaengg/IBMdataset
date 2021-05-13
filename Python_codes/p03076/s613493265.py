x,y=[],[]
t=10
for i in range(5):
    x.append(int(input()))
    y.append(x[i]%10)
    if 0<y[i]<t:
        t=y[i]
    if x[i]%10!=0:
        x[i]=((x[i]//10)+1)*10
    y[i]=x[i]
print(sum(y)+t-10)