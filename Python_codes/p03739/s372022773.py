n=int(input())
a=list(map(int,input().split()))
# + - + - 
su=0
op1=0
for i in range(n):
#    print(i,su,end=' i,su\n')
    if i%2==0:
        #su>0
        if su+a[i]<=0:
            diff=1-(su+a[i])
            op1+=diff
            su+=diff
 #           print(i,diff)
    if i%2==1:
        #su<0
        if su+a[i]>=0:
            diff=(su+a[i])+1
            op1+=diff
            su-=diff
  #          print(i,diff)
    su+=a[i]
su=0
op2=0
for i in range(n):
   # print(i,su,end=' i,su\n')
    if i%2==1:
        #su>0
        if su+a[i]<=0:
            diff=1-(su+a[i])
            op2+=diff
            su+=diff
    #        print(i,diff)
    if i%2==0:
        #su<0
        if su+a[i]>=0:
            diff=(su+a[i])+1
            op2+=diff
            su-=diff
     #       print(i,diff)
    su+=a[i]
print(min(op1,op2))
