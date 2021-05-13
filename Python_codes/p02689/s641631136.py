N, M = map(int, input().split())
H = list(map(int, input().split()))
tmp = [list(map(int, input().split())) for _ in range(M)]

A, B = [], []
for t in tmp:
    A.append(t[0])
    B.append(t[1])

is_good_arr = [True] * N

for i in range(M):
    if H[A[i]-1] > H[B[i]-1]:
        is_good_arr[B[i] - 1] = False
    elif H[A[i]-1] < H[B[i]-1]:
        is_good_arr[A[i] - 1] = False 
    else:
        is_good_arr[A[i]-1], is_good_arr[B[i]-1] = False, False

print(is_good_arr.count(True))