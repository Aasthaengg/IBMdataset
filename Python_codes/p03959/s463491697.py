N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

t_left = []
t_right = []
a_left = []
a_right = []
for i in range(N):
    if i == 0:
        t_left.append(T[i])
        t_right.append(T[i])
    else:
        if T[i] > T[i-1]:
            t_left.append(T[i])
            t_right.append(T[i])
        else:
            t_left.append(1)
            t_right.append(T[i])

for i in range(N - 1, -1, -1):
    if i == N - 1:
        a_left.append(A[i])
        a_right.append(A[i])
    else:
        if A[i] > A[i+1]:
            a_left.append(A[i])
            a_right.append(A[i])
        else:
            a_left.append(1)
            a_right.append(A[i])
a_left = a_left[::-1]
a_right = a_right[::-1]
# print(t_left)
# print(t_right)
# print(a_left)
# print(a_right)
ans = 1
MOD = int(1e9) + 7
for i in range(N):
    l = max(t_left[i], a_left[i])
    r = min(t_right[i], a_right[i])
    if l > r:
        print(0)
        exit()
    else:
        ans *= (r - l + 1)
        ans %= MOD
print(ans % MOD)
