a,b,c= map(int,raw_input().split())
n=0
i=a
for i in range(a,b+1):
    if c%i==0:
        n += 1
    i += 1
print n