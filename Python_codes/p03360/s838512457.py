A, B, C = map(int, input().split())
K = int(input())

max_num = max([A, B, C])
max_num = max_num * (2 ** K)
print(sum([A, B, C]) - max([A, B, C]) + max_num)
