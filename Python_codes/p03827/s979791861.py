N = int(input())
S = input()
MAX = 0
Now = 0
for TS in range(0,N):
    Now += [-1,1][S[TS]=='I']
    MAX = max(MAX,Now)
print(MAX)