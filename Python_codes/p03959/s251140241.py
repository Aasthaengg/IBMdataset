N = int(raw_input())
T_list = map(int, raw_input().split())
A_list = map(int, raw_input().split())

low_list = [1]*N
high_list = [1]*N

t_now = 0
for i in range(N):
    if T_list[i] > t_now:
        t_now = T_list[i]
        low_list[i] = T_list[i]
        high_list[i] = T_list[i]
    else:
        high_list[i] = T_list[i]
a_now = 0
for j in range(N):
    i = N - 1 - j
    if A_list[i] > a_now:
        a_now = A_list[i]
        low_list[i] = max(A_list[i], low_list[i])
        high_list[i] = min(A_list[i], high_list[i])
    else:
        high_list[i] = min(A_list[i], high_list[i])
    
res = 1
for i in range(N):
    if high_list[i] < low_list[i]:
        res = 0
        break
    else:
        res = res*(high_list[i] - low_list[i] + 1) % 1000000007

print res