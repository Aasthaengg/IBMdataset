N, M, C = map(int,input().split())
B = list(map(int,input().split()))
A_list = [list(map(int,input().split())) for _ in range(N)]

correct = 0
for A in A_list:
    sum_ab = C
    for a, b in zip(A, B):
        sum_ab += a*b
    if sum_ab > 0:
        correct += 1

print(correct)