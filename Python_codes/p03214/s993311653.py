N = int(input())

N_list = list(map(int,input().split()))

N_avg = sum(N_list)/N
N_avg_list=[]
for i in range(N):
  N_avg_list.append(abs(N_list[i]-N_avg))
  
print(N_avg_list.index(min(N_avg_list)))