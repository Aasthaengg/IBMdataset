import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
S = readline().decode().rstrip()
R_cnt = S.count('R')
G_cnt = S.count('G')
B_cnt = S.count('B')
ans1 = R_cnt * G_cnt * B_cnt
cnt  = 0
d_max = N // 2 +1
for d in range(1,d_max):
    for i in range(N):
        if i+2*d >= N:
            break
        if (S[i] != S[i+d]) and (S[i+d] != S[i+2*d]) and (S[i] !=S[i+2*d]):
           cnt += 1
ans = ans1 - cnt
print(ans)