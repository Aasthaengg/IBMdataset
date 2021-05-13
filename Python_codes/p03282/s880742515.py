import sys
input = sys.stdin.readline

S = input()
K = input()
if len(S) <= int(K):
    a = len(S)
else:
    a = int(K)
for i in range(a):
    ans = S[i]
    if ans != '1':
        print(ans)
        exit()
print(ans)
