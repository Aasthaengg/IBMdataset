N = int(input())

A_list = list()
B_list = list()

for i in range(N):
    A,B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

print(min(A_list)-1 + max(A_list)-min(A_list)+1 +min(B_list))