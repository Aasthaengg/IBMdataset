N,M = map(int,input().split())

AC = [0]*N
WA = [0]*N
AC_cnt = 0
WA_cnt = 0

p = [0]*M
S = [0]*M

for i in range(M):
    p[i],S[i] = map(str, input().split())

for i in range(M):
    q_num = int(p[i])
    if AC[q_num-1] == 0:
        if S[i] == "AC":
            AC[q_num-1] = 1
        else:
            WA[q_num-1] += 1

for i in range(N):
    if AC[i] == 1:
        WA_cnt += WA[i]
        AC_cnt += 1

print(AC_cnt,WA_cnt)
