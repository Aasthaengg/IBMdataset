S = input().strip()
K = int(input())
N = len(S)
ind = N
for i in range(N):
    if S[i]!="1":
        ind = i
        break
if K<=ind:
    print(1)
else:
    print(S[ind])