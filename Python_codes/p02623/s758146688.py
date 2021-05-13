N, M, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
A_sum_list = [0]
B_sum_list = [0]

for i in range(0,N):
    A_sum_list.append(A_sum_list[i]+A_list[i])
for i in range(0,M):
    B_sum_list.append(B_sum_list[i]+B_list[i])
time = 0
number = 0
j = M

for i in range(0,N+1):
    if A_sum_list[i] > K:
        break 
    while K - A_sum_list[i] < B_sum_list[j]: 
        j -= 1
    number = max(number, i+j)
print(number)