n = int(input())
a = list(map(int,input().split()))
cm = 1000
p1 = p2 = a[0]
for i in range(1,n):
    #print(i,a[i],p1,p2)
    if(a[i]>=p2):
        p2 = a[i]
    elif(a[i]<p2):
        cm += (cm//p1)*(p2-p1)
        p1 = p2 = a[i]
cm += (cm//p1)*(p2-p1)
print(cm)
