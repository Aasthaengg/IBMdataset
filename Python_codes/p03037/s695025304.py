n,m=list(map(int,input().split()))
l_list=[]
r_list=[]
for i in range(m):
  l,r=list(map(int,input().split()))
  l_list.append(l)
  r_list.append(r)

ans_1=max(l_list)
ans_2=min(r_list)
print(max(ans_2-ans_1+1,0))
