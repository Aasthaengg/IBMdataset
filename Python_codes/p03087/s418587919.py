N,Q = map(int,input().split())
S = input()
AC = [0]*N
cnt = 0
for i in range(1,N):
    if S[i-1:i+1] == 'AC':
        cnt += 1
    AC[i] = cnt
        
for i in range(Q):
    l,r = map(int,input().split())
    print(AC[r-1]-AC[l-1])