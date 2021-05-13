# input
A = list(map(int, input().split()))

#check
A.sort()
cost = 0
for idx, a in enumerate(A):
    if idx == 0:
        continue
    else:
        cost += a - A[idx - 1]
print(cost)