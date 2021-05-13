A = []
b = []

n, m = map(int, input().split())
for i in range(n):
    A.append([int(i) for i in input().split()])
for i in range(m):
    b.append(int(input()))

# with open('input_itp1_6_d_1.txt', mode='r', encoding='utf8') as f:
#     n, m = map(int, next(f).split())
#     try:
#         for i in range(n):
#                 A.append([int(i) for i in next(f).split()])
#         for i in range(m):
#             b.append(int(next(f)))
#     except StopIteration:
#         raise ValueError('入力データがおかしい')

c = []
for i in range(len(A)):
    tmp = 0
    for j in range(len(A[i])):
        tmp += A[i][j] * b[j]
    c.append(tmp)
for i in range(len(c)):
    print(c[i])
