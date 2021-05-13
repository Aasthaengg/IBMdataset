N = int(input())

S = input()

min_num = N+1

W = []
E = []

w_cnt = 0
e_cnt = 0

for i in range(N):
    if S[i] == 'W':
        w_cnt += 1
    W.append(w_cnt)

for i in range(N-1,0,-1):
    min_num = min(min_num,W[i-1]+e_cnt)
    if S[i] == 'E':
        e_cnt += 1

print(min(min_num,e_cnt))

