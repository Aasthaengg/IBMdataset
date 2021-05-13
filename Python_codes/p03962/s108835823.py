a,b,c=map(int,input().split())
 
l=sum([a==b,b==c,c==a])
print([3,2,0,1][l])