N = int(input())
A = list(map(int, input().split()))
amax = max(A)
max_idx = A.index(amax)
amin = min(A)
min_idx = A.index(amin)

ans_list = []
if amax*amin < 0:
    if abs(amax) >= abs(amin):
        for i in range(N):
            A[i] += amax
            ans_list.append([max_idx+1, i+1])
    else:
        for i in range(N):
            A[i] += amin
            ans_list.append([min_idx+1, i+1])

# print(A)
amax = max(A)
amin = min(A)

if amax > 0:
    for i in range(N-1):
        ans_list.append([i+1, i+2])
elif amin < 0:
    for i in range(N-1, 0, -1):
        ans_list.append([i+1, i])

print(len(ans_list))
for i in range(len(ans_list)):
    print(*ans_list[i])
