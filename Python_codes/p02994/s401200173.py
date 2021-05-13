N,L=map(int,input().split())
taste=[0]*N; abs_taste=[0]*N;
for i in range(N):
  taste[i]=L+i
  abs_taste[i]=abs(L+i)
for i in range(N):
  if abs_taste[i]==min(abs_taste) :
    min_i=i
    break
print(sum(taste)-taste[min_i])