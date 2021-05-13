N,K=list(map(int,input().split()))
X=list(map(int,input().split()))

P_list=[0]
N_list=[0]
zero_num=0

for x in X:
    if x < 0:
        N_list.append(-x)
    elif x == 0:
        zero_num=1
    else:
        P_list.append(x)
        
K=K-zero_num

P_list.sort()
N_list.sort()
P_list,N_list

move=[]
for i in range(K+1):
    j=K-i
#     print(i,j)
    if i >= len(P_list) or j >= len(N_list):
        continue
    move_=min(2*P_list[i]+N_list[j],P_list[i]+2*N_list[j])
#     print(move_)
    move.append(move_)
    
if len(move)==0:
    move.append(0)
    
print(min(move))