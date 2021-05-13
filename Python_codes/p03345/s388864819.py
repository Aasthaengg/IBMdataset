A, B, C, K = map(int, input().split())
# threshold = 10 ** 18
res = (-1) ** K * (A - B)
# if abs(res) > threshold:
    # print('Unfair')
# else:
    # print(res)
print(res)