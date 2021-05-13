N,K,Q = map(int,input().split())
num_list = [0]*N
for i in range(Q):
  j = int(input())
  num_list[j-1]+=1
  
for i in range(N):
  if K-Q+num_list[i]>0:
    print('Yes')
  else:
    print('No')