N = int(input())
A = [0] * (N + 1)
A = list(map(int,input().split()))
# for i in range(N):
#     A[i] = int(i)
cMoney = 1000
stock = 0
A.append(0)
# for i in range(N):
#     if i == N - 1:
#         if stock > 0:
#             cMoney += A[i] * stock
#             stock = 0
#         continue

#     if A[i] >= A[i+1]:
#         if stock > 0:
#             cMoney += A[i] * stock
#             stock = 0
#     else:
#         stock = cMoney // A[i]
#         cMoney -= stock * A[i]

# print(cMoney)

for i in range(N):
    stock = 0
    if A[i] < A[i+1]:
        stock = cMoney // A[i]

    cMoney += (A[i+1] - A[i]) * stock
print(cMoney)