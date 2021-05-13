n = int(input())
A = list(map(int, input().split()))
A.sort()


# print(A)
# t = 0
# for k in range(1, n):
#     # print("A[0:{}]={}".format(k, A[:k]))
#     # print("{} <? {}".format(2 * sum(A[:k]), A[k]))
#     if 2 * sum(A[:k]) < A[k]:
#         t = max(t, k)

t = 0
value = A[0]
for k in range(1, n):
    # print("A[0:{}]={}".format(k, A[:k]))
    # print("{} <? {}".format(2 * sum(A[:k]), A[k]))
    if 2 * value < A[k]:
        t = max(t, k)
    value += A[k]


print(n - t)

