n,a,b=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]

dif=[x[ind+1]-x[ind] for ind in range(len(x)-1)]
c=0
for i in dif:
    if(i*a > b):
        c+=b
    else:
        c+=i*a
print(c)