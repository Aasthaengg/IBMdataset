S = list(input())
n = len(S)
cnt_b = 0
cnt = 0
for i in range(n):
    if S[i] == 'B':
        cnt_b += 1
        cnt += i
ans = int((2*n - cnt_b -1)*cnt_b*0.5 - cnt)
print(ans)