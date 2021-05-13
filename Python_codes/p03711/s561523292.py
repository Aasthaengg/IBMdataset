x,y = map(int,input().split())

A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
C = [2]
ans = 'No'
if (x in A) and (y in A):
  ans ='Yes'
elif (x in B) and (y in B):
  ans ='Yes'
elif (x in C) and (y in C):
  ans ='Yes'
  
print(ans)