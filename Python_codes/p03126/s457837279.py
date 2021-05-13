n,m=map(int,input().split())
ans_list=list(input().split())[1:]
for i in range(n-1):
  l=len(ans_list)
  ans_list2=ans_list
  ans_list=[]
  keep=input().split()[1:]
  for j in range(l):
    if ans_list2[j] in keep:
      ans_list.append(ans_list2[j])
print(len(ans_list))