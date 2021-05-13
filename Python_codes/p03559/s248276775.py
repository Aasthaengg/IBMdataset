n=int(input())
arr1=sorted(list(map(int,input().split())),reverse=True)
arr2=sorted(list(map(int,input().split())),reverse=True)
arr3=sorted(list(map(int,input().split())),reverse=True)
cnt=[0]*n
ans=0
pos=0
for i in range(n):
  for j in range(pos,n):
    if arr1[j]<arr2[i]:
      cnt[i]=n-pos
      break
    else:
      pos+=1
pos=0
for i in range(n):
  for j in range(pos,n):
    if arr2[i]<arr3[j]:
      pos+=1
    else:
      ans+=cnt[i]*pos
      break
  else:
    ans+=cnt[i]*pos
print(ans)