(N,K) = map(int,input().split())
S = input()
dan = 1

for i in range(N-1):
    if S[i] != S[i+1]:
        dan += 1

if 2*K >= (dan-1):
    print(N-1)
else:
    print(N-dan+2*K)