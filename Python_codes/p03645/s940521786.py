N,M = map(int,input().split())
a_list=[]
pass_1= []
for i in range(M):
    a = list(map(int,input().split()))
    if(a[0]==1):
        pass_1.append(a[1])
    elif(a[1]==N):
        a_list.append(a[0])
    
if list(set(pass_1) & set(a_list)):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')