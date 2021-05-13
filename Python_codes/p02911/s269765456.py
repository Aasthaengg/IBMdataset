N, K, Q = map(int, input().split())
A = Q - K 
N_dict = {}
for i in range(1,N+1):
    N_dict[i] = 0

for i in range(Q):
    N_dict[int(input())] +=1

for i in range(1,N+1):
    if  N_dict[i] > A:
        print('Yes')
        continue
    print('No')