def T(N,A):
    t = 1
    for i in range(N):
        if A[i]%2 == 1:
            t = 0
    return t

def W(b):
    return b/2

N = int(input())
A = list(map(int,input().split()))
count = 0
t = T(N,A)
while t == 1:
    A = list(map(W,A))
    count += 1
    t = T(N,A)
print(count)

