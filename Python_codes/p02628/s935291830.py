n,k=map(int,input().split())
array=list(map(int,input().split()))
new_list_reverse = sorted(array)
ans=0
for i in range(k):
  ans=ans+new_list_reverse[i]
print(ans)