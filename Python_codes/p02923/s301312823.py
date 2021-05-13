n =int(input())
H = list(map(int,input().split()))

c=0
cmax=0
for i in range(n-1):
    if H[i]>=H[i+1] :
        c+=1
    else:
        cmax = max(c,cmax)
        c=0
cmax = max(c,cmax)
print(cmax)
