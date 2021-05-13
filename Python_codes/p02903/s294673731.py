h,w,a,b=map(int,input().split());x='01'
for i in range(h):print(x[i<b]*a+x[i>=b]*(w-a))