N = int(input())

A_list = list()

for i in range(N):
    A = input()
    A_list.append(A)

ans = len(set(A_list))
print(ans)