
N = int(input())
A = list(map(int,input().split()))

A_odd = 0
A_eve = 0

for i in range(N):
    if i % 2 ==0:
        A_eve += A[i]
    else:
        A_odd += A[i]

ans_list = []
for i in range(N):
    if i ==0:
        ans = A_eve-A_odd
    else:
        ans = -ans + A[i - 1]*2
    ans_list.append(str(ans))

print(' '.join(ans_list))