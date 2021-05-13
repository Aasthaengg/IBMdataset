a,b,c=map(int,raw_input().split())
ct=0
for i in xrange(a,b+1):
    if c%i==0:
        ct+=1
    else :
        continue
print(ct)