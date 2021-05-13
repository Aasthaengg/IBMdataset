s=input()
n=len(s)
arr1=[]
arr2=[]
for i in range(n):
  if s[i]!='x':
    arr1.append(s[i])
    arr2.append(i)
if len(arr1)==0:
  print(0)
  exit()
for i in range(len(arr1)):
  if arr1[i]!=arr1[len(arr1)-i-1]:
    print(-1)
    exit()
arr2=[0]+arr2+[n-1]
arr3=[]
for i in range(len(arr2)-1):
  arr3.append(arr2[i+1]-arr2[i])
ans=0
for i in range(len(arr3)//2):
  ans+=max(arr3[i],arr3[len(arr3)-i-1])-min(arr3[i],arr3[len(arr3)-i-1])
print(ans)
#print(arr3)