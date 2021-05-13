N,Q = map(int,input().split())
S = input()

t = [0]*(N+1)
for i in range(N):
    t[i+1] = t[i] + (S[i:i+2] == "AC")
    
for i in range(Q):
    l,r = map(int,input().split())
    print(t[r-1]-t[l-1])