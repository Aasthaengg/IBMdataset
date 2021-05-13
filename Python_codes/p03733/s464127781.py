n,t = map(int,input().split())
a = list(map(int,input().split()))

a.append(1000000000000)

an = 0

for i in range(n):
    if(a[i+1]-a[i]>t):
        if(i>0):
            an += t
        elif(i==0):
            an += t
    else:
        an += a[i+1]-a[i]
    
    # print(an)
        
print(an)