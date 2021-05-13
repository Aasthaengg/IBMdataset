N, K = map(int,input().split())
S = input()
s = []
if S[0]=='0':s = [0]
for x in S.replace('01', '0,1').replace('10','1,0').split(','):
    s.append(len(x))
M = len(s)
ans = [0] * M
ans[0] = sum(s[:2*K+1])

for i in range(2, M, 2):
    ans[i] = ans[i-2] - s[i-2] - s[i-1] + sum(s[min(i+2*K-1,M):i+2*K+1])
print(max(ans))