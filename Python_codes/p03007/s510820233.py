N = int(input())
A = list(map(int, input().split()))

A_plus = []
A_minus = []
for i in range(N):
    if A[i] >= 0:
        A_plus.append(A[i])
    else:
        A_minus.append(A[i])

if len(A_plus) == 0:
    A_plus.append(A_minus.pop(A_minus.index(max(A_minus))))
elif len(A_minus) == 0:
    A_minus.append(A_plus.pop(A_plus.index(min(A_plus))))
        
ans_list = []
while len(A_plus) + len(A_minus) != 1:
    if len(A_plus) <= len(A_minus):
        x = A_plus.pop(0)
        y = A_minus.pop(0)
        ans_list.append([x, y])
        A_plus.append(x-y)
    else:
        x = A_minus.pop(0)
        y = A_plus.pop(0)
        ans_list.append([x, y])
        A_minus.append(x-y)

M = A_plus[0]
print(M)
for i in range(len(ans_list)):
    print(ans_list[i][0], ans_list[i][1])