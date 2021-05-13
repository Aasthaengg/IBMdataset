n,x = map(int,input().split())
l = [int(x) for x in input().split()]

save = 1
for i in range(1,n+2):
    if(i==1):
        d = 0
        continue
    d = d + l[i-2]
    if(d > x):
        break
    save = i
    
print(save)