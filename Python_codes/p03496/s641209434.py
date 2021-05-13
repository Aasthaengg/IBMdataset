N = int(input())
A = list(map(int,input().split()))

print(2*N-2)

maxa = max(A)
mina = min(A)

if abs(maxa) > abs(mina):
    maxi = A.index(maxa)
    for i in range(N):
        if i==maxi:
            continue
        print(maxi+1,i+1)
    for i in range(N-1):
        print(i+1,i+2)
        
else:
    mini = A.index(mina)
    for i in range(N):
        if i==mini:
            continue
        print(mini+1,i+1)
    for i in range(N-1):
        print(N-i,N-i-1)