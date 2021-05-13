n,*a=map(int,open(0).read().split())
b=1
for i in a:
    b*=2-i%2
print(pow(3,len(a))-b)