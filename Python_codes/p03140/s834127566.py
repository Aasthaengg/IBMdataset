N = int(input())
A = input()
B = input()
C = input()

res = 0

for i in range(N):
    set_num = len(set([A[i],B[i],C[i]]))
    if set_num == 3:
        res += 2
    elif set_num == 2:
        res += 1

print(res)