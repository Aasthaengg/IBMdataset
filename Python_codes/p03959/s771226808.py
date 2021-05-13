mod = 1000000007
N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
T_max = 0
T_max_i = 0
for i in range(N):
    if T[i] > T_max:
        T_max = T[i]
        T_max_i = i
A_max = 0
A_max_i = 0
for i in range(N):
    if A[i] >= A_max:
        A_max = A[i]
        A_max_i = i
if T_max != A_max or T_max_i > A_max_i:
    print(0)
else:
    ans = 1
    h = 0
    for i in range(T_max_i + 1):
    	if T[i] > h:
    		h = T[i]
    	else:
    		ans = (ans * h) % mod
    for i in range(T_max_i + 1, A_max_i):
    	ans = (ans * h) % mod
    for i in range(A_max_i + 1, N):
    	if A[i] < h:
    		h = A[i]
    	else:
    		ans = (ans * h) % mod
    print(ans)