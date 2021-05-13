n=int(input())
a=list(map(int,input().split()))

a.sort()

#2倍以下なら吸える
#3,1,4
#→3,4

suma=0
cnt=0
for i in range(n-1):
    suma+=a[i]
    if a[i+1]<=2*suma:
        cnt+=1
    else:
        cnt=0
    

print(cnt+1)


    
