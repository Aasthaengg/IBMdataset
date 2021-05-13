N = int(input())
B_list = list(map(int, input().split()))

A_list = [0]*(N+1)
A_list[0] = B_list[0]
A_list[1] = B_list[0]

for i in range(1, N-1):
    A_list[i + 1] = B_list[i]
    if A_list[i + 1] < A_list[i]:
        A_list[i] = A_list[i + 1]
    
print(sum(A_list))