N = int(input())
*A, = map(int, input().split())
max_A, min_A = max(A), min(A)
max_idx, min_idx = A.index(max_A), A.index(min_A)
mode = None
if min_A >= 0: mode = 2
elif max_A <= 0: mode = 3
elif max_A >= abs(min_A): mode = 0
else: mode = 1
actions = []
if mode == 0:
    for i in range(N):
        if i != max_idx:
            A[i] += A[max_idx]; actions.append((max_idx+1, i+1))
    mode += 2
elif mode == 1:
    for i in range(N):
        if i != min_idx:
            A[i] += A[min_idx]; actions.append((min_idx+1, i+1))
    mode += 2
if mode == 2:
    for i in range(N-1):
        A[i+1] += A[i]; actions.append((i+1, i+2))
elif mode == 3:
    for i in range(N-1, 0, -1):
        A[i-1] += A[i]; actions.append((i+1, i))
print(len(actions))
for a in actions: print(*a)