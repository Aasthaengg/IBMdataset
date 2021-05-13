a,b,k = map(int,input().split())
l = []
for i in range(a,min(a+k,b)):
    print (i)
    l.append(i)

for i in range(max(a,b-k+1),b+1):
    if not i in l:
        print (i)
