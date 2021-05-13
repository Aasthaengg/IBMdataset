n,c,k,*t=map(int,open(0).read().split())
t.sort()
s=t[0]#start
ss=0#start
#end=t[i]
p=0
for i in range(n):
    if t[i]-s>k or i-ss+1>c:
        p+=1
        s=t[i]
        ss=i
print(p+1)