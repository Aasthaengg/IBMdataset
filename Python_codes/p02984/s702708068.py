n=int(input())
dam=list(map(int,input().split()))
plus_mainas=-1
x=dam[0]
ans_list=[0]
for i in range(n-1,0,-1):
  x+=plus_mainas*dam[i]
  plus_mainas*=-1
ans_list.append(x)

for i in range(1,n):
  ans_list.append(dam[i]*2-ans_list[i])

print(*([ans_list[-1]]+ans_list[1:-1]))