# v=[]
# num=251
# for i in range(num):
#     if i==0 or i==1:
#         v.append(1)
#     else:
#         v.append(i*v[i-2])
        
# for i in range(0,num,2):
#     print(i,v[i],end=' ')
#     print()

n=int(input())
if n%2!=0:
    print(0)
else:
    ans=n//10
    n=n//10
    i=1
    while(1):
        ans+=n//(5**i)
        if n//(5**i)==0:
            break
        i+=1
        
        
    print(ans)