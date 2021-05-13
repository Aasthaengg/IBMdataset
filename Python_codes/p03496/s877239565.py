N = int(input())
A = list(map(int,input().split()))
maxa = -float('inf')
mina = float('inf')
for i,a in enumerate(A):
    if maxa < a:
        maxa = a
        maxi = i
    if mina > a:
        mina = a
        mini = i

if abs(maxa) >= abs(mina):
    print(2*N-1)
    for i in range(N):
        print(maxi+1,i+1)
    for i in range(N-1):
        print(i+1,i+2)

else:
    print(2*N-1)
    for i in range(N):
        print(mini+1,i+1)
    for i in range(N,1,-1):
        print(i,i-1)