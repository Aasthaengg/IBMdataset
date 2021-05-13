n=int(input())
s=100000
a=1
a=a+1
for i in range(n):
    if (s*1.05)%1000==0:
        s=s*1.05
    else:
        s=s*1.05-(s*1.05)%1000+1000
print(int(s))
