N = int(input())
A = list(map(int,input().split()))

dis_cnt = 1
for a in A:
  if(a%2 == 0):
    dis_cnt = dis_cnt*2
  else:
    dis_cnt = dis_cnt*1
    
ans = 3**N - dis_cnt 
print(ans)