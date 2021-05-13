N, Q = map(int, input().split())
S = input()
a = [0]*(N+1)
for i in range(N):
    if S[i:i+2] == 'AC':
        a[i+1] = a[i] + 1
    else:
        a[i+1] = a[i]
for _ in range(Q):
    b, c = map(int, input().split())
    print(a[c-1]-a[b-1])    
