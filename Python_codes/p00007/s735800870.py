n=int(raw_input())
g,r=100000,1.05
for i in range(n):
    g*=r
    if int(g)%1000>0:
        g=(int(g)/1000)*1000+1000
print g