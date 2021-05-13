A, B, C, D = [list(map(int, input().split())) for i in range(4)]

tr = min(A, B)
bu = min(C, D)
print(tr[0] + bu[0])
