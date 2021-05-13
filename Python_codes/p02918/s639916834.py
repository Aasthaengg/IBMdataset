N, K = map(int, input().split())
Ss = input().rstrip()

num = Ss.count('LR') + Ss.count('RL')
num -= 2*K
if num < 0:
    num = 0

ans = N - (num+1)
print(ans)
