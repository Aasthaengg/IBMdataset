N, Q = map(int, input().split())
S = input()
t = S.count('AC')
L = [0]
R = [0]
for i in range(N-1):
    L.append(L[i]+1 if S[i:i+2] == 'AC' else L[i])
    R.append(R[i]+1 if S[N-i-2:N-i] == 'AC' else R[i])
R.reverse()
for i in range(Q):
    l, r = map(int, input().split())
    print(t-L[l-1]-R[r-1])
