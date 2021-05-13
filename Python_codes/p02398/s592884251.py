a,b,c = map(int,raw_input().split())
t=0
for i in range(a,b+1):
    if not c%i:
        t+=1
print t