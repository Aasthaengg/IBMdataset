d={1:1,3:1,5:1,7:1,8:1,10:1,12:1,4:2,6:2,9:2,11:2,2:3}
a=list(map(int,input().split()))
if d[a[0]]==d[a[1]]: 
    print('Yes')
else: 
    print('No')