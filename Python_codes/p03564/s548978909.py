N=int(input())
K=int(input())
cur_val=1
for i in range(0,N):
  cur_val=min(cur_val*2,cur_val+K)
print(cur_val)
