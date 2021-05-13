N,K = map(int, input().split())
S = input()
k = 0
for i in range(N):
    if i != N-1 and S[i] == 'R' and S[i] == S[i+1]:
        k += 1
    elif i != 0 and S[i] == 'L' and S[i] == S[i-1]:
        k += 1
k = k + 2*K
if k > N-1:
    print(N-1)
else:
    print(k)