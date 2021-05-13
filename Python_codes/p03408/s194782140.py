N = int(input()) 
S = [input() for _ in range(N)]
new_S = set(S)
M = int(input()) 
T = [input() for _ in range(M)]
use = 0
for i in new_S:
    use1 = S.count(i) - T.count(i) 
    use = max(use,use1)

print(use)